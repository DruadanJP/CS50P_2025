def main():
    text = input("camelCase: ")
    vowels = "a,e,i,o,u"
    for char in vowels:
        text = text.replace(char,"")
    print(text)
    
    
main()