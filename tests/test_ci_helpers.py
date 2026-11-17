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
def test_parse_dependency_files(value, expected):
    assert parse_dependency_files(value) == expected


def test_parse_dependency_files_removes_duplicates():
    value = "\n".join(
        [
            "pyproject.toml",
            "requirements.txt",
            "",
            "pyproject.toml",
            "  requirements.txt  ",
        ]
    )

    result = parse_dependency_files(value)

    assert result == [
        Path("pyproject.toml"),
        Path("requirements.txt"),
    ]