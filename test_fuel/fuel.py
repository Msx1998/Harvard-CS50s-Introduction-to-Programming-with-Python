def main():
    print(gauge(convert(input("Fraction: "))))


def convert(fraction):
    while True:
        try:
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)
            z = x / y
            if z <= 1:
                return int(z*100)
            else:
                fraction = input("Fraction:")
                pass
        except (ValueError,ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
