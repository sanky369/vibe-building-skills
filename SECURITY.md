# Security Guidelines

## API Key Management

This repository contains skills and tools that integrate with external APIs (FAL.ai for creative asset generation). Proper security practices are essential to protect your API keys and prevent unauthorized access.

### ⚠️ Critical: Never Commit API Keys

**DO NOT:**
- ❌ Hardcode API keys in code files
- ❌ Commit `.env` files with real keys
- ❌ Share API keys in pull requests or issues
- ❌ Store keys in version control history
- ❌ Paste keys into documentation or comments

**DO:**
- ✅ Use environment variables for all API keys
- ✅ Use `.env` files locally (and add to `.gitignore`)
- ✅ Rotate keys regularly
- ✅ Use separate keys for development and production
- ✅ Restrict key permissions to minimum necessary scope

## Setting Up API Keys Securely

### 1. Create a Local Environment File

Create a `.env` file in the project root (this file is in `.gitignore` and won't be committed):

```bash
# .env (DO NOT COMMIT THIS FILE)
FAL_API_KEY=your_actual_api_key_here
```

### 2. Load Environment Variables

**For Python Scripts:**

```python
import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("FAL_API_KEY")
if not api_key:
    raise ValueError("FAL_API_KEY environment variable not set")
```

**For Command Line:**

```bash
# Set environment variable before running
export FAL_API_KEY="your_actual_api_key"

# Or load from .env file
source .env
python creative_cli.py generate-product-photo "Blue headphones"
```

**For Claude Code:**

```
"I'm using the image-generation skill. Can you help me generate images?
I've set my FAL_API_KEY environment variable."
```

### 3. Using with Docker

If you're containerizing this project:

```dockerfile
# Dockerfile
FROM python:3.11

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

# DO NOT copy .env file
# Instead, pass secrets at runtime

CMD ["python", "creative_cli.py"]
```

Run with secrets:

```bash
docker run --env FAL_API_KEY="your_key" your-image
```

## Creative Skills Security

### Python Automation

All Python modules (`fal_api.py`, `creative_cli.py`, `claude_integration.py`) properly handle API keys:

**✅ Correct Implementation:**

```python
# fal_api.py
class NanobananProClient:
    def __init__(self, api_key: Optional[str] = None):
        # Try environment variables first
        self.api_key = api_key or os.getenv("FAL_API_KEY") or os.getenv("FAL_KEY")
        if not self.api_key:
            raise ValueError("FAL_API_KEY or FAL_KEY not found...")
```

### Claude Skills

All creative skills reference environment variables, not hardcoded keys:

**✅ Correct in Skills:**

```markdown
## Setup

1. Set your API key:
   export FAL_API_KEY="your_api_key"

2. Verify it's set:
   echo $FAL_API_KEY
```

**❌ Never in Skills:**

```markdown
# WRONG - DO NOT DO THIS
export FAL_API_KEY="sk-1234567890abcdef"
```

## Audit Results

### ✅ Current Status

- **No hardcoded API keys found** in any skill files
- **No actual keys in git history** (only placeholder examples)
- **Proper environment variable handling** in all Python modules
- **`.gitignore` configured** to prevent accidental commits

### Files Audited

**Creative Skills:**
- ✅ `skills/creative/00-orchestrator/SKILL.md`
- ✅ `skills/creative/01-creative-strategist/SKILL.md`
- ✅ `skills/creative/02-image-generation/SKILL.md`
- ✅ `skills/creative/03-product-photography/SKILL.md`
- ✅ `skills/creative/04-product-video/SKILL.md`
- ✅ `skills/creative/05-social-graphics/SKILL.md`
- ✅ `skills/creative/06-brand-asset/SKILL.md`
- ✅ `skills/creative/07-talking-head/SKILL.md`

**Python Modules:**
- ✅ `docs/fal_api.py` — Uses `os.getenv()` for API key
- ✅ `docs/creative_cli.py` — Passes environment variables
- ✅ `docs/claude_integration.py` — Inherits from fal_api.py
- ✅ `docs/examples.py` — Shows correct setup

## Best Practices

### 1. Key Rotation

Rotate your API keys periodically:

```bash
# Get new key from FAL.ai dashboard
# Update your .env file
export FAL_API_KEY="new_key_here"

# Test that it works
python creative_cli.py test
```

### 2. Separate Keys for Different Environments

```bash
# Development
export FAL_API_KEY="dev_key_xxx"

# Production
export FAL_API_KEY="prod_key_yyy"

# Testing
export FAL_API_KEY="test_key_zzz"
```

### 3. Monitor API Usage

Regularly check your FAL.ai dashboard for:
- Unusual usage patterns
- Unexpected charges
- Failed authentication attempts

### 4. Restrict Key Permissions

When creating API keys in FAL.ai:
- Use the minimum necessary permissions
- Restrict to specific IP addresses if possible
- Set rate limits
- Use read-only keys where applicable

### 5. Secure Local Development

```bash
# Use a password manager for API keys
# Store in 1Password, LastPass, etc.

# Load securely:
export FAL_API_KEY=$(op read op://vault/fal-api-key/password)

# Or use direnv for automatic loading
# .envrc file (not committed)
export FAL_API_KEY="your_key"
```

## If Your Key is Compromised

1. **Immediately revoke the key** in FAL.ai dashboard
2. **Generate a new key**
3. **Update your `.env` file** with the new key
4. **Check your usage** for any unauthorized activity
5. **Review git history** to ensure no keys were committed
6. **Notify your team** if applicable

## Reporting Security Issues

If you discover a security issue in this repository:

1. **Do NOT open a public issue**
2. **Do NOT commit the issue details**
3. **Contact the maintainers privately**
4. **Provide details of the vulnerability**
5. **Allow time for a fix before disclosure**

## Additional Resources

- [OWASP: API Security](https://owasp.org/www-project-api-security/)
- [FAL.ai Security Documentation](https://docs.fal.ai/security)
- [Environment Variables Best Practices](https://12factor.net/config)
- [Git Security: Removing Sensitive Data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)

## Checklist

Before using the creative skills:

- [ ] I have created a `.env` file locally
- [ ] I have added `.env` to `.gitignore`
- [ ] I have set `FAL_API_KEY` in my `.env` file
- [ ] I have verified the key works: `python docs/creative_cli.py test`
- [ ] I understand not to commit my `.env` file
- [ ] I will rotate my key periodically
- [ ] I will monitor my API usage

---

**Remember:** API keys are like passwords. Treat them with the same security you'd use for your bank account. Never share them, never commit them, never hardcode them.

Stay secure! 🔒
