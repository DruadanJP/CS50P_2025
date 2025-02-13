import inflect

p = inflect.engine()


def main():
    name_list = []
    while True:
        try:
            name_list.append(input("Name: "))
        except EOFError:
            break
    print(f"Adieu, adieu, to", p.join(name_list))


if __name__ == "__main__":
    main()
