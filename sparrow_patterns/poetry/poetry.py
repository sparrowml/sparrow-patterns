from pathlib import Path
from typing import Optional

from jinja2 import Environment

from sparrow_patterns.utils import get_source_directory


def poetry(
    project_name: str,
    version: str = "0.1.0",
    description: str = "",
    license: Optional[str] = None,
    cli: bool = False,
    gpu: bool = False,
    project_directory: str = ".",
) -> None:
    """
    Write a .devcontainer directory for the project.

    Parameters
    ----------
    project_name
        The slug for the project. Should be the same as the GitHub repo.
    version
        Semantic version for the project.
    description
        A description of the project. Defaults to blank.
    license
        The license of the package. Optional.
    cli
        Whether this is for a CLI.
    gpu
        Whether to make the GPU available.
    project_directory
        Where to create the .devcontainer folder. Defaults to working directory.
    """
    env = Environment(autoescape=True)
    source_directory = get_source_directory(project_name)
    template_directory = Path(__file__).parent / "templates"
    output_directory = Path(project_directory)
    template_variables = dict(
        project_name=project_name,
        source_directory=source_directory,
        version=version,
        description=description,
        license=license,
        cli=cli,
        gpu=gpu,
    )
    filename = "pyproject.toml"
    with open(template_directory / filename) as f:
        template = env.from_string(f.read())
    with open(output_directory / filename, "w") as f:
        f.write(template.render(**template_variables))
