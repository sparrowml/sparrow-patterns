"""Tests for hello function."""
import pytest

from .example import hello


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Jeanette", "Hello Jeanette!"),
        ("Raven", "Hello Raven!"),
        ("Maxine", "Hello Maxine!"),
    ],
)
def test_hello(name, expected):
    """Example test with parametrization."""
    assert hello(name) == expected
