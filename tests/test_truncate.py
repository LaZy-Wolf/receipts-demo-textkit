from textkit import truncate


def test_short_text_unchanged():
    assert truncate("short", 10) == "short"


def test_exact_width_unchanged():
    assert truncate("hello", 5) == "hello"


def test_no_placeholder():
    assert truncate("hello world", 5, placeholder="") == "hello"
