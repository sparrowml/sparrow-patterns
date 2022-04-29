import os
from pathlib import Path


def devcontainer(project_name: str) -> None:
    """Write a .devcontainer directory for the project."""
    devcontainer_directory = Path(__file__).parent / ".devcontainer"
    print(os.listdir(devcontainer_directory))
