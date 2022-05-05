import os
import tempfile

from .poetry import poetry


def test_adds_optional_packages():
    with tempfile.TemporaryDirectory() as project_directory:
        poetry(
            project_name="foo-bar",
            gpu=True,
            project_directory=project_directory,
        )
        pyproject_path = os.path.join(project_directory, "pyproject.toml")
        assert os.path.exists(pyproject_path)
        with open(pyproject_path) as f:
            assert "torchvision" in f.read()
