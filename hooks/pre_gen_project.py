#!/usr/bin/env python
"""Pre-generation hooks for cookiecutter."""

import re
import sys


def validate_project_slug(project_slug: str) -> None:
    """Validate that project_slug is a valid Python package name."""
    pattern = r"^[a-z][a-z0-9_]*$"
    if not re.match(pattern, project_slug):
        print(f"ERROR: '{project_slug}' is not a valid Python package name!")
        print("Package names must:")
        print("  - Start with a lowercase letter")
        print("  - Contain only lowercase letters, numbers, and underscores")
        sys.exit(1)


def main() -> None:
    """Run pre-generation validation."""
    project_slug = "{{ cookiecutter.project_slug }}"
    validate_project_slug(project_slug)


if __name__ == "__main__":
    main()
