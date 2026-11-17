from pathlib import Path

import pytest

from my_project import parse_dependency_files


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("", []),
        ("\n\n\n", []),
        (
            """
            
            
            """,
            [],
        ),
        (
            "pyproject.toml",
            [Path("pyproject.toml")],
        ),
        (
            """
            pyproject.toml
            requirements.txt
            requirements-dev.txt
            """,
            [
                Path("pyproject.toml"),
                Path("requirements.txt"),
                Path("requirements-dev.txt"),
            ],
        ),
    ],
)
def test_parse_dependency_files
