import os
import tempfile

from .devcontainer import devcontainer


def test_project_name_converts_to_source_directory():
    with tempfile.TemporaryDirectory() as project_directory:
        devcontainer(
            project_name="foo-bar",
            project_directory=project_directory,
        )
        source_directory = "foo_bar"
        config_path = os.path.join(project_directory, ".devcontainer/devcontainer.json")
        with open(config_path) as f:
            assert source_directory in f.read()
