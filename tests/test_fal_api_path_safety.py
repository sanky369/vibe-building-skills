import importlib.util
import tempfile
import unittest
from pathlib import Path

FAL_API_PATH = Path(__file__).resolve().parents[1] / "docs" / "fal_api.py"
_spec = importlib.util.spec_from_file_location("fal_api", FAL_API_PATH)
assert _spec is not None and _spec.loader is not None
_fal_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_fal_mod)
CreativeAssetGenerator = _fal_mod.CreativeAssetGenerator
_sanitize_segment = _fal_mod._sanitize_segment


class TestFalApiPathSafety(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.out_dir = Path(self.tmp.name) / "assets"
        self.gen = CreativeAssetGenerator(api_key="test-key", output_dir=str(self.out_dir))
        self.gen.client.generate_image = lambda **kwargs: {
            "images": [{"url": "https://example.com/mock.png"}]
        }
        self.gen.client.download_image = self._mock_download

    def tearDown(self):
        self.tmp.cleanup()

    def _mock_download(self, image_url: str, output_path: str) -> str:
        p = Path(output_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b"\x89PNG\r\n\x1a\n")
        return str(p)

    def test_rejects_path_traversal_and_absolute_paths(self):
        payloads = ["../../../etc/evil", "/tmp/escape", "..\\..\\win_escape", "C:\\temp\\escape"]
        for bad in payloads:
            with self.subTest(payload=bad):
                with self.assertRaises(ValueError):
                    self.gen.generate_product_photo(product_name=bad, prompt="p")
                with self.assertRaises(ValueError):
                    self.gen.generate_social_graphic(platform=bad, topic="t", prompt="p")
                with self.assertRaises(ValueError):
                    self.gen.generate_brand_asset(asset_type="logo", brand_name=bad, prompt="p")
                with self.assertRaises(ValueError):
                    self.gen.generate_custom(asset_category=bad, asset_name="n", prompt="p")

    def test_slashes_in_topic_and_product_name_stay_flat(self):
        res = self.gen.generate_social_graphic(
            platform="LinkedIn",
            topic="A/B Funnel & 3D Scorecard",
            prompt="clean graphic",
        )
        saved = Path(res["saved_paths"][0]).resolve()
        self.assertTrue(saved.is_relative_to(self.out_dir.resolve()))
        self.assertEqual(saved.parent.name, "linkedin")
        self.assertIn("a_b_funnel_3d_scorecard", saved.name)

    def test_arabic_nfc_and_bidi_control_sanitization(self):
        # Includes RLO (\u202e) spoofing control + Arabic vocalized product name
        seg = _sanitize_segment("\u202eمُنتَج سَحابي 2026\u202c", sep="-")
        self.assertNotIn("\u202e", seg)
        self.assertNotIn("\u202c", seg)
        self.assertIn("مُنتَج-سَحابي-2026", seg)

        res = self.gen.generate_product_photo(
            product_name="\u202eمُنتَج سَحابي\u202c",
            prompt="studio shot",
        )
        saved = Path(res["saved_paths"][0]).resolve()
        self.assertTrue(saved.is_relative_to(self.out_dir.resolve()))
        self.assertTrue(saved.exists())


if __name__ == "__main__":
    unittest.main()
