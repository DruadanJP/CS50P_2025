def main():
    text = input("camelCase: ")
    for char in text:
        if char.isupper():
            text = text.replace(char, "_" + char.lower())
    print(text)


main()
