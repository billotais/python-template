"""CLI application using Typer."""

import typer
from rich.console import Console

from {{ cookiecutter.project_slug }} import __version__
from {{ cookiecutter.project_slug }}.core.config import settings

app = typer.Typer(
    name="{{ cookiecutter.project_slug }}",
    help="{{ cookiecutter.project_description }}",
    add_completion=False,
)
console = Console()


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        console.print(f"{settings.app_name} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version and exit.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """{{ cookiecutter.project_description }}"""


@app.command()
def hello(
    name: str = typer.Argument("World", help="Name to greet"),
) -> None:
    """Say hello to someone."""
    console.print(f"[green]Hello, {name}![/green]")


@app.command()
def goodbye(
    name: str = typer.Argument("World", help="Name to say goodbye to"),
    formal: bool = typer.Option(False, "--formal", "-f", help="Use formal goodbye"),
) -> None:
    """Say goodbye to someone."""
    if formal:
        console.print(f"[blue]Goodbye, {name}. It was a pleasure.[/blue]")
    else:
        console.print(f"[blue]Bye, {name}![/blue]")


if __name__ == "__main__":
    app()
