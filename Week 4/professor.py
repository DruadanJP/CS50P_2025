import random
def main():
    level = get_level()
    z = 10  # Math Questions
    points = 0

    while z > 0:
        # Generate integers using the provided level
        try:
            x = generate_integer(level)
            y = generate_integer(level)
        except ValueError:
            print("Error generating integers. Level must be 1, 2, or 3.")
            continue

        result = x + y  # The correct result

        for _ in range(3):  # Allow up to 3 attempts
            try:
                answer = int(input(f"{x} + {y} = "))  # Prompt user
                if answer == result:
                    points += 1  # Add to score if correct
                    break  # Exit retry loop
                else:
                    print("EEE")  # Incorrect answer
            except ValueError:
                print("EEE")  # Handle invalid inputs
        else:
            print(f"The correct answer was {result}.")  # After 3 failed attempts

        z -= 1  # Decrement the question counter

    print(f"Score: {points}")



def get_level():
    while True:
        try:
            level = int(input("Level? "))
            if level in [1, 2, 3]:  # Only accept 1, 2, or 3
                return level  # Return valid level
            else:
                print("Invalid level. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)  # Return one integer
    elif level == 2:
        return random.randint(10, 99)  # Return one integer
    elif level == 3:
        return random.randint(100, 999)  # Return one integer
    else:
        raise ValueError("Level must be 1, 2, or 3.")


if __name__ == "__main__":
    main()
