months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        x = convert(input("Enter your input: "))
        if "Invalid" not in x:
            print(x)
            break


def convert(x):
    if "/" in x:
        m, d, y = x.split("/")
        if m[0].isalpha():
            return "Invalid input"
        if int(m) > 12 or int(m) < 1:
            return "Invalid month"
        elif int(d) > 31 or int(d) < 1:
            return "Invalid day"
        else:
            m = m.strip()
            d = d.strip()
            y = y.strip()
            if len(m) == 1:
                m = "0" + m
            if len(d) == 1:
                d = "0" + d
            return f"{y}-{m}-{d}"
    elif "," in x:
        t, y = x.split(",")
        if t[0].isnumeric():
            return "Invalid input"
        m, d = t.split()
        m = m.strip()
        d = d.strip()
        y = y.strip()
        if int(d) > 31 or int(d) < 1:
            return "Invalid day"
        if months.index(m) + 1 < 10:
            m = "0" + str(months.index(m) + 1)
        else:
            m = str(months.index(m) + 1)
        if int(d) < 10:
            d = "0" + d
        return f"{y}-{m}-{d}"
    else:
        return "Invalid input"


main()
