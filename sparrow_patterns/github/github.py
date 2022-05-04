from pathlib import Path


def github(project_directory: str = ".") -> None:
    """
    Write a .github directory for the project.

    Parameters
    ----------
    project_directory
        Where to create the .devcontainer folder. Defaults to working directory.
    """
    template_directory = Path(__file__).parent / "templates"
    output_directory = Path(project_directory) / ".github/workflows"
    filename = "build.yml"
    with open(template_directory / filename) as f:
        file_string = f.read()
    with open(output_directory / filename, "w") as f:
        f.write(file_string)
