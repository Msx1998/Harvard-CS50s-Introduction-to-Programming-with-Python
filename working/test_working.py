import pytest
from working import convert


def main():
    test_stuff()


def test_stuff():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    try:
        convert("9 to 5 PM")
        assert False, "ValueError not raised for incorrect format"
    except ValueError:
        pass
    try:
        convert("13:00 AM to 5:00 PM")
        assert False, "ValueError not raised for incorrect hour"
    except ValueError:
        pass
    try:
        convert("9:60 AM to 5:00 PM")
        assert False, "ValueError not raised for incorrect minute"
    except ValueError:
        pass
    try:
        convert("9:00 AM - 5:00 PM")
        assert False, "ValueError no to"
    except ValueError:
        pass
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"


if __name__ == "__main__":
    main()
