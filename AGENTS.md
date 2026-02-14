# AGENTS.md - Guidelines for AI Coding Agents

This is a **cookiecutter template** repository for generating Python projects. When working here, understand you're editing Jinja2 templates, not regular Python files.

## Repository Structure

```
python-template/
├── cookiecutter.json              # Template variables
├── hooks/                         # Pre/post generation scripts
│   ├── pre_gen_project.py
│   └── post_gen_project.py
└── {{cookiecutter.project_slug}}/ # Template directory (Jinja2)
    ├── src/{{cookiecutter.project_slug}}/
    ├── tests/
    ├── pyproject.toml
    ├── justfile
    └── ...
```

## Build/Lint/Test Commands

### For This Template Repository

```bash
# Generate a test project
cookiecutter . --no-input project_name="Test Project" app_type=cli

# Generate with specific options
cookiecutter . --no-input project_name="My API" app_type=api use_docker=True
```

### For Generated Projects (using just)

```bash
# Install dependencies
just install-dev          # Install with dev dependencies

# Running tests
just test                 # Run all tests
just test tests/test_cli.py                    # Run single test file
just test tests/test_cli.py::test_hello_default  # Run single test
just test -k "hello"      # Run tests matching pattern
just test-cov             # Run with coverage

# Linting and formatting
just lint                 # Check with ruff
just fmt                  # Format and auto-fix
just typecheck            # Type check with ty
just check                # Run all checks (lint + typecheck + test)

# Other commands
just run                  # Run the application
just clean                # Remove build artifacts
just build                # Build package
just pre-commit           # Run pre-commit hooks
```

### Direct Commands (without just)

```bash
uv sync --all-extras                           # Install dependencies
uv run pytest                                  # Run all tests
uv run pytest tests/test_api.py::test_health   # Run single test
uv run pytest -k "test_hello"                  # Pattern match
uv run ruff check src tests                    # Lint
uv run ruff format src tests                   # Format
uv run ty check src                            # Type check
```

## Code Style Guidelines

### Formatting (Ruff)

- **Line length**: 88 characters
- **Quote style**: Double quotes (`"`)
- **Indent style**: Spaces (4)
- **Trailing commas**: Yes, for multi-line structures

### Import Order (isort via Ruff)

Imports are sorted in this order:
1. Standard library
2. Third-party packages
3. First-party (project) imports

```python
# Standard library
from collections.abc import AsyncIterator
from pathlib import Path

# Third-party
from fastapi import FastAPI
from pydantic import BaseModel

# First-party
from my_project import __version__
from my_project.core.config import settings
```

### Type Annotations

- **Always** use type hints for function parameters and return types
- Use `-> None` for functions that don't return a value
- Use modern syntax: `dict[str, int]` not `Dict[str, int]`
- Use `collections.abc` for abstract types: `AsyncIterator`, `Sequence`
- Use union syntax: `int | str` not `Union[int, str]`

```python
def get_item(item_id: int) -> dict[str, int | str]:
    """Get a specific item."""
    return {"id": item_id, "name": f"Item {item_id}"}

async def list_items() -> dict[str, list]:
    """List all items."""
    return {"items": []}
```

### Naming Conventions

- **Functions/variables**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private**: Prefix with `_` (e.g., `_project_root`)
- **Unused parameters**: Prefix with `_` (e.g., `_app: FastAPI`)

### Docstrings

- Use triple double quotes
- First line is a brief description ending with period
- Keep docstrings concise

```python
def hello(name: str) -> None:
    """Say hello to someone."""
    print(f"Hello, {name}!")

@pytest.fixture
async def client() -> AsyncClient:
    """Create async test client."""
    ...
```

### Error Handling

- Use specific exception types
- For CLI apps using Typer, raise `typer.Exit()` for clean exits
- For FastAPI, use `HTTPException` with appropriate status codes

### Ruff Lint Rules Enabled

```
E, W    - pycodestyle (errors, warnings)
F       - Pyflakes
I       - isort
B       - flake8-bugbear
C4      - flake8-comprehensions
UP      - pyupgrade
ARG     - flake8-unused-arguments
SIM     - flake8-simplify
TCH     - flake8-type-checking
PTH     - flake8-use-pathlib
RUF     - Ruff-specific rules
```

**Ignored**: `E501` (line too long - handled by formatter)

### Testing Patterns

- Test files: `tests/test_*.py`
- Test functions: `def test_*() -> None:`
- Use `pytest.fixture` for setup
- Async tests are auto-detected (`asyncio_mode = "auto"`)

```python
# CLI testing
from typer.testing import CliRunner
runner = CliRunner()

def test_hello() -> None:
    """Test hello command."""
    result = runner.invoke(app, ["hello", "World"])
    assert result.exit_code == 0
    assert "Hello, World!" in result.stdout

# API testing
@pytest.fixture
async def client() -> AsyncClient:
    """Create async test client."""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        yield ac

async def test_endpoint(client: AsyncClient) -> None:
    """Test API endpoint."""
    response = await client.get("/health")
    assert response.status_code == 200
```

### Configuration (Dynaconf)

- Settings in `settings.toml` (committed)
- Secrets in `.secrets.toml` (not committed)
- Override via environment: `PROJECT_SLUG_SETTING_NAME=value`
- Switch environments: `PROJECT_SLUG_ENV=production`

## Template-Specific Notes

When editing files in `{{cookiecutter.project_slug}}/`:

1. **Jinja2 syntax is expected** - LSP errors about `{{ cookiecutter.* }}` are normal
2. **Conditionals** use `{% if cookiecutter.app_type == 'cli' %}`
3. **Filters**: `{{ cookiecutter.project_slug | upper }}` for transformations
4. **Test changes** by generating a project: `cookiecutter . --no-input`

## Pre-commit Hooks

Hooks run automatically on commit:
- trailing-whitespace
- end-of-file-fixer
- check-yaml
- check-added-large-files
- check-merge-conflict
- detect-private-key
- ruff (lint + format)
