import fire

from .devcontainer import devcontainer
from .dockerfile import dockerfile
from .github import github
from .poetry import poetry
from .vscode import vscode


def main() -> None:
    """Call CLI commands."""
    fire.Fire(
        {
            "devcontainer": devcontainer,
            "dockerfile": dockerfile,
            "github": github,
            "poetry": poetry,
            "vscode": vscode,
        }
    )
