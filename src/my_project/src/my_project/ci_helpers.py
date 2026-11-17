from pathlib import Path

PathList = list[Path]


def parse_dependency_files(value: str) -> PathList:
    if not isinstance(value, str):
        raise TypeError(
            f"value must be str, got {type(value).__name__}"
        )

    result: PathList = []
    seen = set()

    for raw_line in value.splitlines():
        line = raw_line.strip()

        if not line:
            continue

        path = Path(line)

        if path in seen:
            continue

        seen.add(path)
        result.append(path)

    return result