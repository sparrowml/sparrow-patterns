import os
from pathlib import Path

from jinja2 import Environment


def dockerfile(
    gpu: bool = False,
    deepstream: bool = False,
    project_directory: str = ".",
) -> None:
    """
    Write a Dockerfile the project.

    Parameters
    ----------
    gpu
        Whether to make the GPU available
    deepstream
        Whether to set up project for DeepStream
    project_directory
        Where to create the .devcontainer folder. Defaults to working directory.
    """
    env = Environment(autoescape=True)
    template_directory = Path(__file__).parent / "templates"
    output_directory = Path(project_directory)
    template_variables = dict(gpu=gpu, deepstream=deepstream)
    for fname in os.listdir(template_directory):
        output_path = output_directory / fname
        with open(template_directory / fname) as f:
            template = env.from_string(f.read())
        with open(output_path, "w") as f:
            f.write(template.render(**template_variables))
