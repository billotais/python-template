"""Tests for CLI application."""

from typer.testing import CliRunner

from {{ cookiecutter.project_slug }}.cli import app

runner = CliRunner()


def test_hello_default() -> None:
    """Test hello command with default argument."""
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert "Hello, World!" in result.stdout


def test_hello_with_name() -> None:
    """Test hello command with custom name."""
    result = runner.invoke(app, ["hello", "Alice"])
    assert result.exit_code == 0
    assert "Hello, Alice!" in result.stdout


def test_goodbye_default() -> None:
    """Test goodbye command with default argument."""
    result = runner.invoke(app, ["goodbye"])
    assert result.exit_code == 0
    assert "Bye, World!" in result.stdout


def test_goodbye_formal() -> None:
    """Test goodbye command with formal flag."""
    result = runner.invoke(app, ["goodbye", "Bob", "--formal"])
    assert result.exit_code == 0
    assert "Goodbye, Bob. It was a pleasure." in result.stdout


def test_version() -> None:
    """Test version flag."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "v0.1.0" in result.stdout
