import inflect
import sys
from datetime import date

i = inflect.engine()

def main():
    user_input = input("Birth Date YYYY-MM-DD:")
    y, m, d = validate(user_input)
    b = date(int(y), int(m), int(d))
    t = date.today()
    tt = t - b
    tm = tt.days* 24 * 60
    o = i.number_to_words(tm,andword="")
    print(o.capitalize()+" minutes")

def validate(user_input):
    try:
        date.fromisoformat(user_input)
        return user_input.split("-")
    except ValueError:
        sys.exit(1)

if __name__ == "__main__":
    main()
