def main():
    # Ask for input from the user
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    # Define the vowels to remove
    vowels = "aeiouAEIOU"

    # Loop through each vowel in the string "aeiou"
    for char in vowels:
        # Replace every occurrence of the vowel in 'text' with an empty string (removing it)
        word = word.replace(char,"",)
    # Print the modified text after all vowels are removed
    return word


if __name__ == "__main__":
    main()
