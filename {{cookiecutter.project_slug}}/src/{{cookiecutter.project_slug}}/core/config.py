"""Application configuration using Dynaconf."""

from pathlib import Path

from dynaconf import Dynaconf

# Get the project root directory
_project_root = Path(__file__).parent.parent.parent.parent

settings = Dynaconf(
    envvar_prefix="{{ cookiecutter.project_slug | upper }}",
    settings_files=[
        _project_root / "settings.toml",
        _project_root / ".secrets.toml",
    ],
    environments=True,
    load_dotenv=True,
    env_switcher="{{ cookiecutter.project_slug | upper }}_ENV",
)

# Usage:
# - Access settings: settings.app_name, settings.debug, etc.
# - Switch environment: export {{ cookiecutter.project_slug | upper }}_ENV=production
# - Override via env vars: export {{ cookiecutter.project_slug | upper }}_DEBUG=true
