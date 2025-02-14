# Modules to import
import csv
import sys
from typing import IO
import os

# Check for errors trough sys.argv
if len(sys.argv) != 3:
    print("Too few command-line arguments")
    sys.exit(1)
if len(sys.argv) >= 4:
    print("Too many command-line arguments")
    sys.exit(1)
if not sys.argv[1].endswith("csv"):
    print("Not a CSV file")
    sys.exit(1)
if not os.path.exists(sys.argv[1]):
    print("File does not exist")
    sys.exit(1)


# Main Function
def main():
    with open("sys.argv[1]", "r") as before, open(
        "sys.argv[2]", "w"
    ) as after:  # type: IO[str]
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last, first = (row["name"]).split(",")
            house = row["house"]
            first = first.strip()
            last = last.strip()
            writer.writerow({"first": first, "last": last, "house": house})


# Call Main Function
if __name__ == "__main__":
    main()
