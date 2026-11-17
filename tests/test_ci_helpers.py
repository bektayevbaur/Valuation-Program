from pathlib import Path
from typing import List

import pytest

from my_project import parse_dependency_files


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("", []),
        ("\n\n\n", []),
        ("   \n\t\n   \n", []),
        (
            "pyproject.toml",
            [Path("pyproject.toml")],
        ),
        (
            "pyproject.toml\nrequirements.txt\nrequirements-dev.txt",
            [
                Path("pyproject.toml"),
                Path("requirements.txt"),
                Path("requirements-dev.txt"),
            ],
        ),
    ],
)
def test_parse_dependency_files(value: str, expected: List[Path]) -> None:
    assert parse_dependency_files(value) == expected


def test_parse_dependency_files_strips_whitespace() -> None:
    value = "  pyproject.toml  \n\trequirements.txt\t"

    assert parse_dependency_files(value) == [
        Path("pyproject.toml"),
        Path("requirements.txt"),
    ]


def test_parse_dependency_files_removes_duplicates() -> None:
    value = "\n".join(
        [
            "pyproject.toml",
            "requirements.txt",
            "",
            "pyproject.toml",
            "  requirements.txt  ",
        ]
    )

    assert parse_dependency_files(value) == [
        Path("pyproject.toml"),
        Path("requirements.txt"),
    ]


def test_parse_dependency_files_rejects_non_str() -> None:
    with pytest.raises(TypeError):
        parse_dependency_files(None)  # type: ignore[arg-type]
