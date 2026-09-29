# textkit

Small, dependency-free text helpers for Python 3.9+.

```python
from textkit import slugify, truncate, parse_duration, format_duration, snake_case

slugify("Hello World")        # 'hello-world'
truncate("hello world", 8)    # shortened text ending in '...'
parse_duration("90s")         # 90
format_duration(5400)         # '1h 30m'
snake_case("helloWorld")      # 'hello_world'
```

## Development

```bash
pip install -e ".[test]"
pytest
```

## Function reference

| Function | What it does |
| --- | --- |
| `slugify(text, sep="-")` | Lowercase, strip accents, replace anything that is not `a-z0-9` with `sep`. |
| `truncate(text, width, placeholder="...")` | Return `text` unchanged if it fits, otherwise cut it and append `placeholder`. |
| `parse_duration(text)` | Parse `d`, `h`, `m`, `s` units (for example `"1h30m"`) into seconds. |
| `format_duration(seconds)` | The inverse of `parse_duration`, for example `5400` becomes `"1h 30m"`. |
| `snake_case(text)` | Convert camelCase, PascalCase, spaces and dashes to snake_case. |

## Contributing

Open an issue first for anything bigger than a bug fix. Every change needs a test in `tests/`.
