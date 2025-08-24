# qa-ui-playwright-python
Python-based UI automation with GitHub Actions CI.

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
pip install pytest pytest-playwright
playwright install
pytest
