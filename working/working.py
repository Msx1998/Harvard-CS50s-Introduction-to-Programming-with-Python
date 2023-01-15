"""
Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

Conversion Table
In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


...


if __name__ == "__main__":
    main()
Either before or after you implement convert in working.py, additionally implement, in a file called test_working.py, three or more functions that collectively test your implementation of convert thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_working.py
"""
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_format = re.compile(r"^(?P<start_hour>\d{1,2}):*(?P<start_minute>\d{2})* (?P<start_am_pm>[AP]M) to (?P<end_hour>\d{1,2}):*(?P<end_minute>\d{2})* (?P<end_am_pm>[AP]M)$")
    match = time_format.search(s)
    if match is None:
        raise ValueError("Invalid time format")
    start_hour = match.group("start_hour")
    start_minute = match.group("start_minute")
    start_am_pm = match.group("start_am_pm")
    end_hour = match.group("end_hour")
    end_minute = match.group("end_minute")
    end_am_pm = match.group("end_am_pm")
    if int(start_hour) > 12 or int(end_hour) > 12:
        raise ValueError("Invalid hour")
    if start_minute is not None and int(start_minute) > 59:
        raise ValueError("Invalid minute")
    if end_minute is not None and int(end_minute) > 59:
        raise ValueError("Invalid minute")
    start_time = new_format(start_hour, start_minute, start_am_pm)
    end_time = new_format(end_hour, end_minute, end_am_pm)
    return f"{start_time} to {end_time}"


def new_format(hour, minute, am_pm):
    new_hour = int(hour)
    if am_pm == "PM" and new_hour != 12:
        new_hour += 12
    elif am_pm == "AM" and new_hour == 12:
        new_hour = 0
    new_minute = ":00" if minute is None else f":{minute}"
    new_time = f"{new_hour:02}{new_minute}"
    return new_time


if __name__ == "__main__":
    main()
