from pathlib import Path


def github(project_directory: str = ".") -> None:
    """
    Write a .github directory for the project.

    Parameters
    ----------
    project_directory
        Where to create the .github folder. Defaults to working directory.
    """
    template_directory = Path(__file__).parent / "templates"
    output_directory = Path(project_directory) / ".github/workflows"
    filename = "build.yml"
    output_directory.mkdir(parents=True, exist_ok=True)
    with open(template_directory / filename) as f:
        file_string = f.read()
    with open(output_directory / filename, "w") as f:
        f.write(file_string)
