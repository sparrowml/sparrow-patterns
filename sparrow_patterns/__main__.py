import fire

from .devcontainer import devcontainer
from .dockerfile import dockerfile
from .poetry import poetry


def main() -> None:
    """Call CLI commands."""
    fire.Fire(
        {
            "devcontainer": devcontainer,
            "dockerfile": dockerfile,
            "poetry": poetry,
        }
    )
