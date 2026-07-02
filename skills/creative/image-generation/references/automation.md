# Creative automation reference — FAL.ai `fal-ai/nano-banana-pro`

The single source of truth for running the image-generation automation that ships
with this repo. Every creative skill that generates images uses this same stack.
There is exactly **one** model: `fal-ai/nano-banana-pro` on FAL.ai. There are no
"fast"/"quality" model variants and no `guidance_scale`, `inference_steps`, or
pixel-size parameters — anything claiming otherwise is stale.

## Files (paths relative to repo root)

| File | Role |
|---|---|
| `docs/fal_api.py` | `NanobananProClient` (raw API) + `CreativeAssetGenerator` (saves organized assets) |
| `docs/creative_cli.py` | CLI wrapper: `product`, `social`, `brand`, `custom`, `test` subcommands |
| `docs/claude_integration.py` | Convenience functions for agent use: `generate_product`, `generate_social`, `generate_brand`, `generate_asset`, `batch_generate_assets`, `get_summary` |

## Setup

```bash
pip install requests
export FAL_API_KEY="..."   # FAL_KEY also accepted as a fallback
python docs/creative_cli.py test   # generates one test image to verify the key
```

Running `python docs/creative_cli.py ...` from the repo root works — Python puts
the script's own directory on `sys.path`, so the `from fal_api import ...` import
resolves. For the Python API, run from `docs/` or add it to `PYTHONPATH`.

## Generation parameters (the real, complete set)

From `NanobananProClient.generate_image` in `docs/fal_api.py`:

| Parameter | Values | Default | Notes |
|---|---|---|---|
| `prompt` | string | required | The full prompt text |
| `num_images` | 1–4 | 1 | Variations per call |
| `aspect_ratio` | `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` | `1:1` | The only shape control — there is no width×height parameter |
| `resolution` | `1K`, `2K`, `4K` | `2K` | `2K` for most work; `4K` for hero/print; `1K` for cheap drafts |
| `output_format` | `png`, `jpeg`, `webp` | `png` | `png` for graphics and brand assets; `jpeg`/`webp` when file size matters |
| `enable_web_search` | bool | `False` | Lets the model pull current facts (e.g. data-driven infographics) |
| `sync_mode` | bool | `False` | Return image as data URI instead of URL |

## CLI usage

```bash
# Product photography → assets/product-photography/<product-slug>/
python docs/creative_cli.py product \
  --product-name "Luxury Watch" \
  --prompt "..." \
  --aspect-ratio 4:5 --resolution 2K --num-images 3

# Social graphic → assets/social-graphics/<platform>/
# platform ∈ instagram | linkedin | twitter | tiktok | pinterest
python docs/creative_cli.py social \
  --platform instagram --topic "Product Launch" \
  --prompt "..." --aspect-ratio 4:5 --num-images 2

# Brand asset → assets/brand-assets/<brand-slug>/<asset-type>/
# asset-type ∈ logo | icon | pattern | illustration | texture
python docs/creative_cli.py brand \
  --asset-type logo --brand-name "TechCorp" \
  --prompt "..." --aspect-ratio 1:1 --num-images 4

# Anything else → assets/<category>/<name>/
python docs/creative_cli.py custom \
  --category thumbnails --name video-1 \
  --prompt "..." --aspect-ratio 16:9 --format png --web-search

# Verify the API key / connection
python docs/creative_cli.py test
```

Global flag: `--output-dir ./assets` (default `./assets`). All subcommands accept
`--aspect-ratio`, `--resolution`, `--num-images`; `custom` also accepts `--format`
and `--web-search`.

## Python API (agent-friendly helpers)

```python
# run with cwd=docs/ or PYTHONPATH including docs/
from claude_integration import (
    generate_product,        # product_name, description, style=..., lighting=..., background=..., num_variations, resolution, aspect_ratio
    generate_social,         # platform, topic, description, ...
    generate_brand,          # brand_name, element_type, description, ...
    generate_asset,          # category, name, prompt, ... (full control, enable_web_search)
    batch_generate_assets,   # list of {"type": "product"|"social"|"brand"|"custom", ...} dicts
)

result = generate_asset(
    category="product-photography",
    name="luxury-watch",
    prompt="A luxury leather watch with gold accents ...",
)
```

For raw control use `CreativeAssetGenerator` / `NanobananProClient` from
`docs/fal_api.py` directly.

## Output organization and file naming

`CreativeAssetGenerator` saves automatically:

```
assets/
├── product-photography/<product-slug>/   <product>_<n>_<YYYYMMDD_HHMMSS>.png
├── social-graphics/<platform>/           <platform>_<topic>_<n>_<timestamp>.png
├── brand-assets/<brand-slug>/<type>/     <type>_<n>_<timestamp>.png
└── <category>/<name>/                    <name>_<n>_<timestamp>.<ext>
```

Slugs are lowercase with spaces → hyphens (directories) or underscores (filenames).

## Troubleshooting

- **`FAL_API_KEY or FAL_KEY not found`** — export one of the two env vars.
- **No images in the result** — check the key is valid; run `python docs/creative_cli.py test`.
- **Off-style output** — the fix is in the prompt (add the style block from
  `skills/creative/creative-strategist`), not in nonexistent model parameters.
- **Slow generation** — drop `resolution` to `1K`/`2K` and `num_images` to 1.
