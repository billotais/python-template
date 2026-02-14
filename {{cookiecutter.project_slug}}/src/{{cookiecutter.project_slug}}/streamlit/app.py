"""{{ cookiecutter.project_name }} Streamlit Application."""

import streamlit as st

from {{ cookiecutter.project_slug }} import __version__
from {{ cookiecutter.project_slug }}.core.config import settings
from {{ cookiecutter.project_slug }}.utils import format_greeting, generate_sample_data


def main() -> None:
    """Main Streamlit application."""
    st.set_page_config(
        page_title="{{ cookiecutter.project_name }}",
        page_icon=":rocket:",
        layout="wide",
    )

    st.title("{{ cookiecutter.project_name }}")
    st.caption(f"Version {__version__}")

    # Sidebar
    with st.sidebar:
        st.header("Settings")
        st.write(f"Environment: {settings.current_env}")
        st.write(f"Debug: {settings.get('debug', False)}")

        st.divider()
        st.subheader("Data Options")
        n_rows = st.slider("Number of rows", min_value=5, max_value=50, value=10)
        seed = st.number_input("Random seed", min_value=0, max_value=1000, value=42)

    # Main content
    st.header("Welcome!")
    st.write("This app demonstrates using shared code from your project.")

    # Example: Using format_greeting from utils
    st.subheader("Greeting Example")
    st.write("Using `format_greeting()` from `{{ cookiecutter.project_slug }}.utils`:")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Enter your name", value="World")
        formal = st.checkbox("Formal greeting")

    with col2:
        if st.button("Generate Greeting"):
            greeting = format_greeting(name, formal=formal)
            st.success(greeting)

    st.divider()

    # Example: Using generate_sample_data from utils
    st.subheader("Data Generation Example")
    st.write("Using `generate_sample_data()` from `{{ cookiecutter.project_slug }}.utils`:")

    # Generate data using shared utility
    data = generate_sample_data(n_rows=n_rows, seed=seed)

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Generated Data:**")
        st.dataframe(data, width="stretch")

    with col2:
        st.write("**Line Chart:**")
        st.line_chart(data, x="x", y="y")

    # Show code example
    st.divider()
    st.subheader("Code Example")
    st.write("Here's how to use the shared utilities in your own code:")
    st.code(
        """
from {{ cookiecutter.project_slug }}.utils import format_greeting, generate_sample_data
from {{ cookiecutter.project_slug }}.core.config import settings

# Use the greeting utility
message = format_greeting("Alice", formal=True)
print(message)  # "Greetings from {{ cookiecutter.project_name }}, Alice. Welcome."

# Generate sample data
data = generate_sample_data(n_rows=20, seed=123)
print(data)  # {'x': [...], 'y': [...], 'category': [...]}

# Access configuration
print(f"Running in {settings.current_env} environment")
""",
        language="python",
    )


if __name__ == "__main__":
    main()
