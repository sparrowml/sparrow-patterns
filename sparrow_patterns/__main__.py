import fire

from .devcontainer import devcontainer


def main() -> None:
    """Call CLI commands."""
    fire.Fire({"devcontainer": devcontainer})
