import fire

from .dependencies import dependencies
from .devcontainer import devcontainer
from .dockerfile import dockerfile
from .github import github
from .gitignore import gitignore
from .makefile import makefile
from .notebooks import notebooks
from .project import project
from .readme import readme
from .vscode import vscode


def main() -> None:
    """Call CLI commands."""
    fire.Fire(
        {
            "dependencies": dependencies,
            "devcontainer": devcontainer,
            "dockerfile": dockerfile,
            "github": github,
            "gitignore": gitignore,
            "makefile": makefile,
            "notebooks": notebooks,
            "project": project,
            "readme": readme,
            "vscode": vscode,
        }
    )
