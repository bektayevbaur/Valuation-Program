def parse_dependency_files(value: str) -> List```

Полный корректный файл:

```python
from pathlib import Path
from typing import List, Set


def parse_dependency_files(value: str) -> Listif not isinstance(value, str):
        raise TypeError(
            f"value must be str, got {type(value).__name__}"
        )

    result: List[Path] = []
    seen: Set[Path] = set()

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
