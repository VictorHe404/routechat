# RouteChat

BYOK multi-LLM chat with per-message model switching and auto routing.

## Dev setup

```bash
uv sync                 # create .venv and install deps
uv run pytest           # run tests
cp .env.example .env    # then edit values
uv run uvicorn routechat.main:create_app --factory --reload   # http://localhost:8000/docs
uv tool install pre-commit
pre-commit install
```
