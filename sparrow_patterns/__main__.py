import fire

from .devcontainer import devcontainer
from .dockerfile import dockerfile


def main() -> None:
    """Call CLI commands."""
    fire.Fire({"devcontainer": devcontainer, "dockerfile": dockerfile})
