import warnings
from pathlib import Path
from typing import Optional

from jinja2 import Environment

from sparrow_patterns.utils import get_source_directory

MAIN_TEMPLATE = """import fire


def main() -> None:
    \"\"\"Call CLI commands.\"\"\"
    fire.Fire()
"""


def dependencies(
    project_name: str,
    version: str = "0.1.0",
    description: str = "",
    license: Optional[str] = None,
    author_name: str = "Sparrow Computing",
    author_email: str = "ben@sparrow.dev",
    project_directory: str = ".",
) -> None:
    """
    Write pyproject.toml for the project.

    Parameters
    ----------
    project_name
        The slug for the project. Should be the same as the GitHub repo.
    version
        Semantic version for the project.
    description
        A description of the project. Defaults to blank.
    license
        The license of the package, e.g. "MIT". Optional.
    author_name
        Project author name
    author_email
        Project author email
    project_directory
        Where to write the files. Defaults to working directory.
    """
    env = Environment(autoescape=True)
    source_directory_string = get_source_directory(project_name)
    source_directory = project_directory / Path(source_directory_string)
    template_directory = Path(__file__).parent / "templates"
    output_directory = Path(project_directory)
    template_variables = dict(
        project_name=project_name,
        source_directory=source_directory_string,
        version=version,
        description=description,
        license=license,
        author_name=author_name,
        author_email=author_email,
    )

    # Create pyproject.toml
    filename = "pyproject.toml"
    with open(template_directory / filename) as f:
        template = env.from_string(f.read())
    with open(output_directory / filename, "w") as f:
        f.write(template.render(**template_variables))

    # Create source directory and files
    source_directory.mkdir(parents=True, exist_ok=True)
    filename = "__init__.py"
    (source_directory / filename).touch()
    filename = "__main__.py"
    if not (source_directory / filename).exists():
        with open(source_directory / filename, "w") as f:
            f.write(MAIN_TEMPLATE)

    # Check for legacy files
    if (output_directory / "setup.cfg").exists() or (
        output_directory / "setup.py"
    ).exists():
        message = (
            "setup.cfg and setup.py are no longer needed with pyproject.toml. "
            "You might want to delete them."
        )
        warnings.warn(message)
