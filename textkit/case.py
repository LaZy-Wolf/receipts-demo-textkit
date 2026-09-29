import re


def snake_case(text: str) -> str:
    """Convert camelCase, PascalCase or spaced text to snake_case."""
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", text)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    # Split letters from digits too, so every word boundary is treated the same way.
    s = re.sub(r"([A-Za-z])([0-9])", r"\1_\2", s)
    s = re.sub(r"[\s\-_]+", "_", s)
    return s.strip("_").lower()
