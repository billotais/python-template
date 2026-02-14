"""Tests for utility functions."""

from {{ cookiecutter.project_slug }}.utils import format_greeting, generate_sample_data


def test_format_greeting_casual() -> None:
    """Test casual greeting format."""
    result = format_greeting("Alice")
    assert "Alice" in result
    assert "Hello" in result


def test_format_greeting_formal() -> None:
    """Test formal greeting format."""
    result = format_greeting("Dr. Smith", formal=True)
    assert "Dr. Smith" in result
    assert "Greetings" in result


def test_generate_sample_data_default() -> None:
    """Test sample data generation with defaults."""
    data = generate_sample_data()
    assert "x" in data
    assert "y" in data
    assert "category" in data
    assert len(data["x"]) == 10
    assert len(data["y"]) == 10
    assert len(data["category"]) == 10


def test_generate_sample_data_custom_rows() -> None:
    """Test sample data generation with custom row count."""
    data = generate_sample_data(n_rows=5)
    assert len(data["x"]) == 5


def test_generate_sample_data_reproducible() -> None:
    """Test that seed produces reproducible results."""
    data1 = generate_sample_data(n_rows=5, seed=42)
    data2 = generate_sample_data(n_rows=5, seed=42)
    assert data1["y"] == data2["y"]


def test_generate_sample_data_categories() -> None:
    """Test that categories are valid."""
    data = generate_sample_data(n_rows=100, seed=42)
    valid_categories = {"A", "B", "C"}
    assert all(cat in valid_categories for cat in data["category"])
