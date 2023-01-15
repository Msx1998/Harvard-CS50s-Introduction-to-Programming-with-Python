from seasons import validate
import pytest


def main():
    test_validate_valid()
    test_validate_invalid()


def test_validate_valid():
    assert validate("1998-10-10") == ["1998","10","10"]


def test_validate_invalid():
    with pytest.raises(SystemExit):
        validate("1998-1-1")
    with pytest.raises(SystemExit):
        validate("1998-10-1")
    with pytest.raises(SystemExit):
        validate("1998-1-10")
    with pytest.raises(SystemExit):
        validate("October 12, 1492")


if __name__ == "__main__":
    main()
