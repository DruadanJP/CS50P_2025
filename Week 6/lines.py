import sys
import os

# Defined Variables
line_count = 0

# Check for errors trough sys.argv
if len(sys.argv) != 2:
    print("Too few command-line arguments")
    sys.exit(1)
if len(sys.argv) >= 3:
    print("Too many command-line arguments")
    sys.exit(1)
if not sys.argv[1].endswith("py"):
    print("Not a Python file")
    sys.exit(1)
if not os.path.exists(sys.argv[1]):
    print("File does not exist")
    sys.exit(1)

# Open the file, specified with the file name trough sys.argv
with open(sys.argv[1], "r") as f:
    try:
        for line in f:
            li = line.strip()
            if li.startswith("#") or line.isspace():
                continue
            else:
                line_count += 1
    except FileNotFoundError:
        raise FileNotFoundError


print(f"Total number of lines: {line_count}")
