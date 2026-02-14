# Python Project Template

A modern Python project template using [cookiecutter](https://cookiecutter.readthedocs.io/).

## Features

- **uv** - Fast Python package and project manager
- **just** - Command runner for common tasks
- **ruff** - Extremely fast Python linter and formatter
- **ty** - Fast Python type checker (from Astral)
- **pytest** - Testing framework with coverage support
- **Docker** - Multi-stage Dockerfile with uv
- **GitHub Actions** - CI/CD workflow
- **pre-commit** - Git hooks for code quality

## App Types

Choose between:
- **CLI** - Command-line application using [Typer](https://typer.tiangolo.com/)
- **API** - Web API using [FastAPI](https://fastapi.tiangolo.com/)

## Requirements

- Python 3.10+
- [cookiecutter](https://cookiecutter.readthedocs.io/) (`pip install cookiecutter` or `uv tool install cookiecutter`)
- [uv](https://docs.astral.sh/uv/) (for generated projects)
- [just](https://github.com/casey/just) (optional, for generated projects)

## Usage

### Generate a new project

```bash
# From GitHub
cookiecutter gh:yourusername/python-template

# Or from local directory
cookiecutter /path/to/python-template
```

### Template options

| Option | Default | Description |
|--------|---------|-------------|
| `project_name` | My Awesome Project | Human-readable project name |
| `project_slug` | (derived) | Python package name |
| `project_description` | A short description... | Project description |
| `author_name` | Your Name | Author name |
| `author_email` | your.email@example.com | Author email |
| `python_version` | 3.12 | Python version |
| `app_type` | cli | Choose: `cli` or `api` |
| `use_docker` | true | Include Dockerfile |
| `use_github_actions` | true | Include CI workflow |
| `license` | MIT | Choose license |

## Generated Project Structure

### CLI Project
```
my_project/
├── src/
│   └── my_project/
│       ├── __init__.py
│       └── cli.py
├── tests/
│   └── test_cli.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── .pre-commit-config.yaml
├── Dockerfile
├── justfile
├── pyproject.toml
└── README.md
```

### API Project
```
my_project/
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── main.py
│       ├── api/
│       │   └── routes.py
│       └── core/
│           └── config.py
├── tests/
│   └── test_api.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── .env.example
├── .pre-commit-config.yaml
├── Dockerfile
├── justfile
├── pyproject.toml
└── README.md
```

## Development

### Test the template locally

```bash
# Generate a test project
cookiecutter . --no-input

# Or with custom options
cookiecutter . project_name="Test CLI" app_type=cli

# Test the generated project
cd test_cli
just install-dev
just check
```

## License

MIT
