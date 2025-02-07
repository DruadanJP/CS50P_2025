def main():
    # Ask for input from the user
    text = input("Input: ").lower()

    # Define the vowels to remove
    vowels = "aeiou"

    # Loop through each vowel in the string "aeiou"
    for char in vowels:
        # Replace every occurrence of the vowel in 'text' with an empty string (removing it)
        text = text.replace(char, "",)

    # Print the modified text after all vowels are removed
    print(text, end="")

main()
