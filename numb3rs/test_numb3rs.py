"""
tests for numb3rs.py
"""
from numb3rs import validate


def main():
    test_is_numeric()
    test_is_in_range()


def test_is_numeric():
    assert validate("10.0.0.1") == True
    assert validate("10.0.0") == False
    assert validate("10.0") == False
    assert validate("1") == False


def test_is_in_range():
    assert validate("255.255.255.255") == True
    assert validate("999.1.1.1") == False
    assert validate("1.999.1.1") == False
    assert validate("1.1.999.1") == False
    assert validate("1.1.1.999") == False


if __name__ == "__main__":
    main()
