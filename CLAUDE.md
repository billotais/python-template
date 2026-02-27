# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

This is a **cookiecutter template repository** that generates Python projects. Files under `{{cookiecutter.project_slug}}/` are Jinja2 templates, not regular Python — LSP errors on `{{ cookiecutter.* }}` expressions are expected.

## Commands

### Template Operations (run from repo root)
```bash
cookiecutter . --no-input                                    # Generate test project with defaults
cookiecutter . --no-input project_name="My API" app_type=api # Generate with options
```

### Generated Project Commands (run from generated project dir)
```bash
just install-dev                                    # Install with dev dependencies
just test                                           # Run all tests
just test tests/test_cli.py                         # Run single test file
just test tests/test_cli.py::test_hello_default     # Run single test
just test -k "hello"                                # Pattern match tests
just test-cov                                       # Tests with coverage
just lint                                           # Lint with ruff
just fmt                                            # Format and auto-fix
just typecheck                                      # Type check with ty
just check                                          # All checks (lint + typecheck + test)
just run                                            # Run application
```

Direct uv equivalents: `uv run pytest`, `uv run ruff check src tests`, `uv run ruff format src tests`, `uv run ty check src`.

## Architecture

### Template Variables (`cookiecutter.json`)
- `app_type`: "cli" (Typer) or "api" (FastAPI) — controls which files are kept
- `use_notebooks`, `use_streamlit`, `use_docker`, `use_github_actions`: toggle optional features
- `python_version`: sets target Python version in ruff and CI configs

### Generation Hooks (`hooks/`)
- `pre_gen_project.py`: validates `project_slug` is a valid Python identifier
- `post_gen_project.py`: removes files based on template options (e.g., removes `cli.py` for API projects, removes `main.py`+`api/` for CLI projects, strips optional features), then initializes git

### Generated Project Layout
```
src/{project_slug}/
├── cli.py          # CLI app (Typer) — only for app_type=cli
├── main.py         # FastAPI app — only for app_type=api
├── api/routes.py   # API routes — only for app_type=api
├── core/config.py  # Dynaconf settings
├── utils/helpers.py
└── streamlit/app.py  # optional
```

### Key Tooling in Generated Projects
- **uv**: package management and virtual environments
- **just** (justfile): task runner
- **ruff**: linting and formatting (line-length 88, double quotes, rules: E/W/F/I/B/C4/UP/ARG/SIM/TCH/PTH/RUF)
- **ty**: type checking
- **pytest**: testing (asyncio_mode=auto, src layout via `pythonpath = ["src"]`)
- **Dynaconf**: configuration via `settings.toml` / `.secrets.toml`, env override pattern: `PROJECT_SLUG_SETTING_NAME=value`

## Code Style

- Type hints required on all function signatures, use modern syntax (`dict[str, int]`, `int | str`, `collections.abc`)
- Naming: `snake_case` functions/variables, `PascalCase` classes, `UPPER_SNAKE_CASE` constants
- Docstrings: triple double quotes, brief first line ending with period
- CLI errors: `typer.Exit()`; API errors: `HTTPException`
- CLI testing: `CliRunner` from `typer.testing`; API testing: `AsyncClient` with `ASGITransport`

## Template Editing Notes

- Use Jinja2 conditionals: `{% if cookiecutter.app_type == 'cli' %}`
- Use Jinja2 filters: `{{ cookiecutter.project_slug | upper }}`
- Always test changes by generating a project: `cookiecutter . --no-input`
