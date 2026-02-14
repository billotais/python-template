"""Helper functions for {{ cookiecutter.project_name }}."""

from {{ cookiecutter.project_slug }}.core.config import settings


def format_greeting(name: str, formal: bool = False) -> str:
    """Format a greeting message.

    Args:
        name: The name to greet.
        formal: Whether to use formal greeting.

    Returns:
        Formatted greeting string.
    """
    app_name = settings.get("app_name", "{{ cookiecutter.project_name }}")
    if formal:
        return f"Greetings from {app_name}, {name}. Welcome."
    return f"Hello, {name}! Welcome to {app_name}."


def generate_sample_data(n_rows: int = 10, seed: int = 42) -> dict[str, list]:
    """Generate sample data for demonstrations.

    Args:
        n_rows: Number of rows to generate.
        seed: Random seed for reproducibility.

    Returns:
        Dictionary with sample data columns.
    """
    import random

    random.seed(seed)

    categories = ["A", "B", "C"]
    cumsum = 0.0
    y_values = []

    for _ in range(n_rows):
        cumsum += random.gauss(0, 1)
        y_values.append(round(cumsum, 4))

    return {
        "x": list(range(1, n_rows + 1)),
        "y": y_values,
        "category": [random.choice(categories) for _ in range(n_rows)],
    }
