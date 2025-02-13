def convert(emoticons):
    return emoticons.replace(":)", "🙂").replace(":(", "🙁")


def main():
    userdata = input("Enter your data: ")
    print(convert(userdata))


main()
