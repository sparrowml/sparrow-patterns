from pathlib import Path


def vscode(project_directory: str = ".") -> None:
    """
    Write a .vscode directory for the project.

    Parameters
    ----------
    project_directory
        Where to create the .vscode folder. Defaults to working directory.
    """
    template_directory = Path(__file__).parent / "templates"
    output_directory = Path(project_directory) / ".vscode"
    filename_stem = ["extensions", "launch", "settings"]
    output_directory.mkdir(exist_ok=True)
    for stem in filename_stem:
        filename = f"{stem}.json"
        with open(template_directory / filename) as f1:
            with open(output_directory / filename, "w") as f2:
                f2.write(f1.read())
