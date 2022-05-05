from pathlib import Path

from jinja2 import Environment

from ..utils import get_source_directory


def makefile(project_name: str, project_directory: str = ".") -> None:
    """
    Write a Makefile directory for the project.

    Parameters
    ----------
    project_name
        The slug for the project. Should be the same as the GitHub repo.
    project_directory
        Where to create the .vscode folder. Defaults to working directory.
    """
    env = Environment(autoescape=True)
    source_directory = get_source_directory(project_name)
    template_directory = Path(__file__).parent / "templates"
    output_directory = Path(project_directory)
    filename = "Makefile"
    template_variables = dict(
        project_name=project_name,
        source_directory=source_directory,
    )
    with open(template_directory / filename) as f:
        template = env.from_string(f.read())
    with open(output_directory / filename, "w") as f:
        f.write(template.render(**template_variables))
