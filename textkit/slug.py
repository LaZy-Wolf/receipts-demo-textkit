import re
import unicodedata


def slugify(text: str, sep: str = "-") -> str:
    """Turn text into a URL-safe slug: 'Hello World' -> 'hello-world'."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]", sep, text.lower())
