from pathlib import Path

from jinja2 import Environment

from sparrow_patterns.utils import get_source_directory


def vscode(project_name: str, project_directory: str = ".") -> None:
    """
    Write a .vscode directory for the project.

    Parameters
    ----------
    project_directory
        Where to create the .vscode folder. Defaults to working directory.
    """
    source_directory = get_source_directory(project_name)
    env = Environment(autoescape=True)
    template_variables = dict(source_directory=source_directory)
    template_directory = Path(__file__).parent / "templates"
    output_directory = Path(project_directory) / ".vscode"
    filename_stem = ["extensions", "launch"]
    output_directory.mkdir(exist_ok=True)
    for stem in filename_stem:
        filename = f"{stem}.json"
        with open(template_directory / filename) as f1:
            with open(output_directory / filename, "w") as f2:
                f2.write(f1.read())
    with open(template_directory / "settings.json") as f:
        template = env.from_string(f.read())
    with open(output_directory / "settings.json", "w") as f:
        f.write(template.render(**template_variables))
