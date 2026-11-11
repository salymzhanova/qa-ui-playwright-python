# QA UI Automation with Python + Playwright

[![UI Tests](https://github.com/salymzhanova/qa-ui-playwright-python/actions/workflows/ci.yml/badge.svg)](https://github.com/salymzhanova/qa-ui-playwright-python/actions/workflows/ci.yml)

## What this repo shows
- UI automation with Python + Playwright
- CI/CD integration using GitHub Actions
- Runs against public demo app (SauceDemo)

## How to run locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
pytest e2e/tests
```

## Notes
- The SauceDemo credentials are the public demo ones. Override the shared
  password with the `SAUCEDEMO_PASSWORD` environment variable if needed.
- Never commit `.env` files or tokens; they are git-ignored.
