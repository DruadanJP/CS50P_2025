# Import the libraries / modules
import sys
from tabulate import tabulate
import csv
import os

# sys.argv checks
if len(sys.argv) != 2:
    print("Usage: python csv.csv <filename>")
    sys.exit(1)
if not sys.argv[1].endswith(".csv"):
    print("Not a Python file")
    sys.exit(1)
if not os.path.exists(sys.argv[1]):
    print("File does not exist")
    sys.exit(1)


# main function
def main():
    pizza = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            pizza.append(row)

    print(tabulate(pizza, headers="keys", tablefmt="grid"))


# call the main function
if __name__ == "__main__":
    main()
