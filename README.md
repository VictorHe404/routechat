# RouteChat

BYOK multi-LLM chat with per-message model switching and auto routing.

## Dev setup

```bash
uv sync                 # create .venv and install deps
uv run pytest           # run tests
uv run uvicorn routechat.main:app --reload   # http://localhost:8000/health
uv tool install pre-commit
pre-commit install
```
