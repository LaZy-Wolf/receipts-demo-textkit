import re
import unicodedata

# Letters that NFKD does not decompose into ASCII, so they would silently vanish.
_TRANSLITERATE = str.maketrans({
    "ß": "ss", "æ": "ae", "Æ": "AE", "ø": "o", "Ø": "O", "đ": "d", "Đ": "D",
    "ł": "l", "Ł": "L", "œ": "oe", "Œ": "OE", "þ": "th", "Þ": "TH",
})


def slugify(text: str, sep: str = "-") -> str:
    """Turn text into a URL-safe slug: 'Hello World' -> 'hello-world'."""
    text = unicodedata.normalize("NFKD", text.translate(_TRANSLITERATE))
    text = text.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]", sep, text.lower())
