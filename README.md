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
