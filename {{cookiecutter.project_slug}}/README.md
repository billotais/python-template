# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Requirements

- Python {{ cookiecutter.python_version }}+
- [uv](https://docs.astral.sh/uv/) - Fast Python package manager
- [just](https://github.com/casey/just) - Command runner (optional but recommended)

## Quick Start

### Installation

```bash
# Install dependencies
just install-dev

# Or without just:
uv sync --all-extras
```

### Running the Application

{% if cookiecutter.app_type == 'cli' %}
```bash
# Run CLI
just run --help

# Or directly:
uv run {{ cookiecutter.project_slug }} --help
```
{% elif cookiecutter.app_type == 'api' %}
```bash
# Run development server
just run

# Or directly:
uv run uvicorn {{ cookiecutter.project_slug }}.main:app --reload

# Access the API at http://localhost:8000
# API docs at http://localhost:8000/docs
```
{% endif %}

{% if cookiecutter.use_streamlit %}
### Streamlit App

```bash
# Run Streamlit app
just streamlit

# Or directly:
uv run streamlit run src/{{ cookiecutter.project_slug }}/streamlit/app.py

# Access the app at http://localhost:8501
```
{% endif %}

{% if cookiecutter.use_notebooks %}
### Jupyter Notebooks

```bash
# Install notebook dependencies
just install-dev

# Start Jupyter Notebook
just notebook

# Or start Jupyter Lab
just lab

# Install kernel for this project
just kernel-install

# Or directly:
uv run --extra notebook jupyter notebook notebooks/
```
{% endif %}

{% if cookiecutter.app_type == 'api' %}
### API Collection

This project includes a [Bruno](https://www.usebruno.com/) API collection in the `bruno/` directory for testing and exploring the API endpoints. Open the collection in Bruno or any compatible client.
{% endif %}

### Development

```bash
# Run tests
just test

# Run tests with coverage
just test-cov

# Lint code
just lint

# Format code
just fmt

# Type check
just typecheck

# Run all checks
just check
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
just setup-hooks

# Run pre-commit on all files
just pre-commit
```

{% if cookiecutter.use_docker %}
### Docker

```bash
# Build image
just docker-build

# Run container
just docker-run
```
{% endif %}

## Configuration

This project uses [Dynaconf](https://www.dynaconf.com/) for configuration management.

### Configuration Files

- `settings.toml` - Main configuration file (committed to git)
- `.secrets.toml` - Sensitive values (not committed to git)
- `.env` - Environment variables (not committed to git)

### Environments

Switch between environments using the `{{ cookiecutter.project_slug | upper }}_ENV` variable:

```bash
# Development (default)
export {{ cookiecutter.project_slug | upper }}_ENV=development

# Production
export {{ cookiecutter.project_slug | upper }}_ENV=production

# Testing
export {{ cookiecutter.project_slug | upper }}_ENV=testing
```

### Override Settings

Override any setting via environment variables with the `{{ cookiecutter.project_slug | upper }}_` prefix:

```bash
export {{ cookiecutter.project_slug | upper }}_DEBUG=true
{% if cookiecutter.app_type == 'api' %}
export {{ cookiecutter.project_slug | upper }}_DATABASE_URL=postgresql://localhost/mydb
{% endif %}
```

### Usage in Code

```python
from {{ cookiecutter.project_slug }}.core.config import settings

# Access settings
print(settings.app_name)
print(settings.debug)
{% if cookiecutter.app_type == 'api' %}
print(settings.database_url)
{% endif %}
```

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/
│   └── {{ cookiecutter.project_slug }}/
{% if cookiecutter.app_type == 'cli' %}
│       ├── __init__.py
│       ├── cli.py           # CLI entry point
{% elif cookiecutter.app_type == 'api' %}
│       ├── __init__.py
│       ├── main.py          # FastAPI application
│       ├── api/
│       │   └── routes.py    # API routes
{% endif %}
{% if cookiecutter.use_streamlit %}
│       ├── streamlit/
│       │   └── app.py       # Streamlit application
{% endif %}
│       ├── utils/
│       │   └── helpers.py   # Helper functions
│       └── core/
│           └── config.py    # Dynaconf configuration
├── tests/
│   └── ...
{% if cookiecutter.use_notebooks %}
├── notebooks/
│   └── getting_started.ipynb
{% endif %}
├── settings.toml            # Configuration file
├── .secrets.toml            # Secrets (not in git)
├── pyproject.toml
├── justfile
└── README.md
```

{% if cookiecutter.license != "None" %}
## License

{{ cookiecutter.license }}
{% endif %}
