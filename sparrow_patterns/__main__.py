import fire

from sparrow_patterns.notebooks.notebooks import notebooks

from .devcontainer import devcontainer
from .dockerfile import dockerfile
from .github import github
from .gitignore import gitignore
from .makefile import makefile
from .notebooks import notebooks
from .package import package
from .poetry import poetry
from .project import project
from .vscode import vscode


def main() -> None:
    """Call CLI commands."""
    fire.Fire(
        {
            "devcontainer": devcontainer,
            "dockerfile": dockerfile,
            "github": github,
            "gitignore": gitignore,
            "makefile": makefile,
            "notebooks": notebooks,
            "package": package,
            "poetry": poetry,
            "project": project,
            "vscode": vscode,
        }
    )
