import re

_UNITS = {"d": 86400, "h": 3600, "m": 60, "s": 1}
_TOKEN = re.compile(r"(\d+)\s*([dhms])")


def parse_duration(text: str) -> int:
    """Parse a duration like '1h30m' or '45s' into seconds."""
    tokens = _TOKEN.findall(text.strip().lower())
    if not tokens:
        raise ValueError(f"invalid duration: {text!r}")
    total = 0
    for value, unit in tokens:
        total += int(value) * _UNITS[unit]
    return total


def format_duration(seconds: int) -> str:
    """Format seconds as a human string: 5400 -> '1h 30m'."""
    parts = []
    for unit, size in _UNITS.items():
        if seconds >= size:
            n, seconds = divmod(seconds, size)
            parts.append(f"{n}{unit}")
    return " ".join(parts) or "0s"
