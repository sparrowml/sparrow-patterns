import os
from pathlib import Path

from jinja2 import Environment

from sparrow_patterns.utils import get_source_directory


def devcontainer(
    project_name: str, aws: bool = False, project_directory: str = "."
) -> None:
    """
    Write a .devcontainer directory for the project.

    Parameters
    ----------
    project_name
        The slug for the project. Should be the same as the GitHub repo.
    aws
        Whether to set up AWS access
    project_directory
        Where to create the .devcontainer folder. Defaults to working directory.
    """
    env = Environment(autoescape=True)
    folder = ".devcontainer"
    source_directory = get_source_directory(project_name)
    template_devcontainer_directory = Path(__file__).parent / folder
    output_devcontainer_directory = Path(project_directory) / folder
    output_devcontainer_directory.mkdir(exist_ok=True)
    template_variables = dict(
        project_name=project_name,
        source_directory=source_directory,
        aws=aws,
    )
    for fname in os.listdir(template_devcontainer_directory):
        output_path = output_devcontainer_directory / fname
        with open(template_devcontainer_directory / fname) as f:
            template = env.from_string(f.read())
        with open(output_path, "w") as f:
            f.write(template.render(**template_variables))
