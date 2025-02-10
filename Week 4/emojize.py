# Import the emoji module
import emoji

def main():
    text = input("Input: ")
    print(emoji.emojize(f"{text}", language='alias'))

if __name__ == '__main__':
    main()
    