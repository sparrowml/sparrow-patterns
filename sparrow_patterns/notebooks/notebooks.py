from pathlib import Path


def notebooks(project_directory: str = ".") -> None:
    """
    Write a notebooks directory for the project.

    Parameters
    ----------
    project_directory
        Where to create the notebooks folder. Defaults to working directory.
    """
    template_directory = Path(__file__).parent / "templates"
    output_directory = Path(project_directory) / "notebooks"
    filename = ".gitignore"
    output_directory.mkdir(exist_ok=True)
    with open(template_directory / filename) as f:
        file_string = f.read()
    with open(output_directory / filename, "w") as f:
        f.write(file_string)
