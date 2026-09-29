import pytest

from textkit import format_duration, parse_duration


def test_parse_seconds():
    assert parse_duration("90s") == 90


def test_parse_hours():
    assert parse_duration("2h") == 7200


def test_parse_is_case_insensitive():
    assert parse_duration("3M") == 180


def test_parse_invalid():
    with pytest.raises(ValueError):
        parse_duration("soon")


def test_format():
    assert format_duration(5400) == "1h 30m"


def test_format_zero():
    assert format_duration(0) == "0s"


def test_format_days():
    assert format_duration(90061) == "1d 1h 1m 1s"
