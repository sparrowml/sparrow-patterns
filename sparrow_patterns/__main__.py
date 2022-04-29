import fire

from .example import hello


def main() -> None:
    """Call CLI commands."""
    fire.Fire({"hello": hello})
