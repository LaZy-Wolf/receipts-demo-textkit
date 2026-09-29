import re


def snake_case(text: str) -> str:
    """Convert camelCase, PascalCase or spaced text to snake_case."""
    s = re.sub(r"([A-Z])", r"_\1", text)
    s = re.sub(r"[\s\-_]+", "_", s)
    return s.strip("_").lower()


def kebab_case(text: str) -> str:
    """Convert camelCase, PascalCase or spaced text to kebab-case."""
    return snake_case(text).replace("_", "-")
