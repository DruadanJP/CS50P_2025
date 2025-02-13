def main():
    # User Input
    x, y, z = input("Expression: ").split()
    match y:
        case "+":
            print(round(float(x) + float(z), 2))
        case "-":
            print(round(float(x) - float(z), 2))
        case "*":
            print(round(float(x) * float(z), 2))
        case "/":
            print(round(float(x) / float(z), 2))


main()
