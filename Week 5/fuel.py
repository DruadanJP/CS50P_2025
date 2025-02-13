import fractions


def main():
    fraction_input = input("Fraction: ")
    percentage = convert(fraction_input)
    print(gauge(percentage))


def convert(fraction):
    try:
        x, y = fraction.strip().split("/")
        x = int(x)
        y = int(y)
        if x > 100 or y > 100:
            raise ValueError
        elif y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        fraction = fractions.Fraction(x, y)
        percentage = fraction * 100
        return int(percentage)
    except ValueError:
        raise ValueError


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{float(percentage):.0f}%"


if __name__ == "__main__":
    main()
