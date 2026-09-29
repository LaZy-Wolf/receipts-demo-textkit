def truncate(text: str, width: int, placeholder: str = "...") -> str:
    """Shorten text to at most `width` characters, ending with `placeholder` if it was cut."""
    if len(text) <= width:
        return text
    if width <= len(placeholder):
        return placeholder[:width]
    return text[: width - len(placeholder)] + placeholder
