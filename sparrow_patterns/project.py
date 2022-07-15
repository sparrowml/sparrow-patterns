from pathlib import Path
from typing import Optional

from slugify import slugify

from .devcontainer import devcontainer
from .dockerfile import dockerfile
from .gitignore import gitignore
from .makefile import makefile
from .poetry import poetry
from .utils import get_source_directory
from .vscode import vscode


def project(
    project_name: str,
    version: str = "0.1.0",
    description: str = "",
    license: Optional[str] = None,
    author_name: str = "Sparrow Computing",
    author_email: str = "ben@sparrow.dev",
    cli: bool = False,
    gpu: bool = False,
    deepstream: bool = False,
    parent_directory: str = ".",
) -> None:
    """Create a new Python package."""
    project_directory = Path(parent_directory) / slugify(project_name)
    project_directory.mkdir(exist_ok=True, parents=True)
    source_directory = project_directory / get_source_directory(project_name)
    source_directory.mkdir(exist_ok=True)
    (source_directory / "__init__.py").touch()
    if cli:
        (source_directory / "__main__.py").touch()
    project_dir_string = str(project_directory)
    devcontainer(
        project_name,
        package=False,
        gpu=gpu,
        project_directory=project_dir_string,
    )
    dockerfile(gpu=gpu, deepstream=deepstream, project_directory=project_dir_string)
    gitignore(project_dir_string)
    makefile(project_name, project_directory=project_dir_string)
    poetry(
        project_name,
        version=version,
        description=description,
        license=license,
        author_name=author_name,
        author_email=author_email,
        cli=cli,
        gpu=gpu,
        project_directory=project_dir_string,
    )
    vscode(project_dir_string)
