import os
import tempfile

from .dockerfile_ import dockerfile


def test_defaults_to_python_image():
    with tempfile.TemporaryDirectory() as project_directory:
        dockerfile("foo-bar", project_directory=project_directory)
        dockerfile_path = os.path.join(project_directory, "Dockerfile")
        with open(dockerfile_path) as f:
            assert "FROM python:3.9" in f.read().splitlines()
