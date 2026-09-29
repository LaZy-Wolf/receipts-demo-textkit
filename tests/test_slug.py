from textkit import slugify


def test_basic():
    assert slugify("Hello World") == "hello-world"


def test_already_slug():
    assert slugify("abc123") == "abc123"


def test_accents_are_stripped():
    assert slugify("Crème Brûlée") == "creme-brulee"


def test_custom_separator():
    assert slugify("a b", sep="_") == "a_b"
