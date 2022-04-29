def get_source_directory(project_name: str) -> str:
    """Get the source directory name from the project name."""
    return project_name.lower().replace(" ", "_").replace("-", "_")
