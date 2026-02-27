#!/usr/bin/env python
"""Post-generation hooks for cookiecutter."""

import os
import shutil
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    """Remove a file from the project directory."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(dirpath: str) -> None:
    """Remove a directory from the project directory."""
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))


def main() -> None:
    """Run post-generation cleanup."""
    app_type = "{{ cookiecutter.app_type }}"
    use_docker = "{{ cookiecutter.use_docker }}".lower() in ("true", "yes", "1")
    use_github_actions = "{{ cookiecutter.use_github_actions }}".lower() in ("true", "yes", "1")
    use_notebooks = "{{ cookiecutter.use_notebooks }}".lower() in ("true", "yes", "1")
    use_streamlit = "{{ cookiecutter.use_streamlit }}".lower() in ("true", "yes", "1")
    license_choice = "{{ cookiecutter.license }}"

    # Remove files based on app type
    if app_type == "cli":
        # Remove FastAPI-related files
        remove_file("src/{{ cookiecutter.project_slug }}/main.py")
        remove_dir("src/{{ cookiecutter.project_slug }}/api")
        remove_file("tests/test_api.py")
        remove_dir("bruno")
    elif app_type == "api":
        # Remove CLI-related files
        remove_file("src/{{ cookiecutter.project_slug }}/cli.py")
        remove_file("tests/test_cli.py")

    # Remove Streamlit files if not using Streamlit
    if not use_streamlit:
        remove_dir("src/{{ cookiecutter.project_slug }}/streamlit")
        remove_file("tests/test_streamlit.py")

    # Remove notebooks directory if not using notebooks
    if not use_notebooks:
        remove_dir("notebooks")

    # Remove Docker files if not using Docker
    if not use_docker:
        remove_file("Dockerfile")
        remove_file(".dockerignore")

    # Remove GitHub Actions if not using them
    if not use_github_actions:
        remove_dir(".github")

    # Remove license file if "None" selected
    if license_choice == "None":
        # Remove LICENSE if it exists
        license_path = os.path.join(PROJECT_DIRECTORY, "LICENSE")
        if os.path.exists(license_path):
            os.remove(license_path)

    # Initialize git repository
    git_ok = False
    try:
        subprocess.run(["git", "init"], check=True, capture_output=True)
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        git_ok = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\nWarning: git initialization failed (is git installed?)")

    print("\n" + "=" * 50)
    print("Project '{{ cookiecutter.project_name }}' created successfully!")
    print("=" * 50)
    print("\nNext steps:")
    print("  cd {{ cookiecutter.project_slug }}")
    if not git_ok:
        print("  git init  # (optional, auto-init failed)")
    print("  just install-dev")
    if app_type == "cli":
        print("  just run --help")
    elif app_type == "api":
        print("  just run")
    if use_streamlit:
        print("  just streamlit")
    if use_notebooks:
        print("  just notebook")
    print("\nHappy coding!")


if __name__ == "__main__":
    main()
