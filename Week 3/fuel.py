import fractions

def main():
    x,y = get_fuel("Fraction: ")
    fraction = fractions.Fraction(x,y)
    percentage = (fraction * 100)
    if percentage > 99 or percentage == 99:
        print("F")
    elif percentage == 0 or percentage == 1:
        print("E")
    else:
        print(f"{float(percentage):.0f}%")

def get_fuel(prompt):
    while True:
        try:
            x,y = (input(prompt)).split("/")
            if int(x) > int(y):
                pass
            else:
                return int(x), int(y)
        except (ValueError, ZeroDivisionError):
            pass

main()
