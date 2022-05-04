import os
import tempfile

from .poetry import poetry


def test_project_name_converts_to_source_directory():
    with tempfile.TemporaryDirectory() as project_directory:
        poetry(
            project_name="foo-bar",
            package=True,
            project_directory=project_directory,
        )
        source_directory = "foo_bar"
        env_example_path = os.path.join(project_directory, ".devcontainer/.env.example")
        gitignore_path = os.path.join(project_directory, ".devcontainer/.gitignore")
        assert os.path.exists(env_example_path) == False
        assert os.path.exists(gitignore_path) == False
        config_path = os.path.join(project_directory, ".devcontainer/devcontainer.json")
        with open(config_path) as f:
            assert source_directory in f.read()
