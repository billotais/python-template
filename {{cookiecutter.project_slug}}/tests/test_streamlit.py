"""Tests for Streamlit app."""

import pytest

from {{ cookiecutter.project_slug }}.streamlit.app import main


def test_main_function_exists() -> None:
    """Test that the main function exists and is callable."""
    assert callable(main)


def test_streamlit_imports() -> None:
    """Test that Streamlit app imports work correctly."""
    # Test that the app module can be imported without errors
    from {{ cookiecutter.project_slug }}.streamlit import app

    assert hasattr(app, "main")


@pytest.mark.skip(reason="AppTest.from_file can timeout in CI environments")
def test_app_runs_integration() -> None:
    """Integration test for Streamlit app (skipped by default)."""
    from pathlib import Path

    from streamlit.testing.v1 import AppTest

    app_path = Path(__file__).parent.parent / "src" / "{{ cookiecutter.project_slug }}" / "streamlit" / "app.py"
    at = AppTest.from_file(str(app_path))
    at.run(timeout=30)
    assert not at.exception
