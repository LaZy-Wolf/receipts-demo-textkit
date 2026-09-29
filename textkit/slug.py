import re
import unicodedata


def slugify(text: str, sep: str = "-") -> str:
    """Turn text into a URL-safe slug: 'Hello World' -> 'hello-world'."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]", sep, text.lower())
    return slug.replace(sep * 2, sep).strip(sep)
