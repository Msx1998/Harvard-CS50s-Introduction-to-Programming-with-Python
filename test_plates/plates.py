def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
        # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if not (2 <= len(s) <= 6):
        return False
    # “All vanity plates must start with at least two letters.”
    if not s[:2].isalpha():
        return False
    # “Numbers cannot be used in the middle of a plate; they must come at the end.
    flag = False
    for c in s:
        if c.isnumeric():
            if c == '0' and not flag:
                return False
            flag = True
        elif c.isalpha():
            if flag:
                return False
        # “No periods, spaces, or punctuation marks are allowed.”
        else:
            return False
    return True


if __name__ == "__main__":
    main()
