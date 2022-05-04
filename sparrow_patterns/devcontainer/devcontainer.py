import os
from pathlib import Path

from jinja2 import Environment

from sparrow_patterns.utils import get_source_directory


def devcontainer(
    project_name: str,
    package: bool = False,
    gpu: bool = False,
    project_directory: str = ".",
) -> None:
    """
    Write a .devcontainer directory for the project.

    Parameters
    ----------
    project_name
        The slug for the project. Should be the same as the GitHub repo.
    package
        Whether this is for a Python package
    gpu
        Whether to make the GPU available
    project_directory
        Where to create the .devcontainer folder. Defaults to working directory.
    """
    env = Environment(autoescape=True)
    source_directory = get_source_directory(project_name)
    template_devcontainer_directory = Path(__file__).parent / "templates"
    output_devcontainer_directory = Path(project_directory) / ".devcontainer"
    output_devcontainer_directory.mkdir(exist_ok=True)
    template_variables = dict(
        project_name=project_name,
        source_directory=source_directory,
        package=package,
        gpu=gpu,
    )
    for fname in os.listdir(template_devcontainer_directory):
        if package and fname in (".env.example", ".gitignore"):
            continue
        output_path = output_devcontainer_directory / fname
        with open(template_devcontainer_directory / fname) as f:
            template = env.from_string(f.read())
        with open(output_path, "w") as f:
            f.write(template.render(**template_variables))
