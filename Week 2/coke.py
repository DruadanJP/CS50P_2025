def main():
    amount_due = 50
    # If correct coins then
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        insert = int(input("Insert Coin: "))
        if insert in (25, 10, 5):
            inserted = insert
            amount_due = amount_due - inserted
        else:
            print(f"Amount Due: {amount_due}")
            insert = int(input("Insert Coin: "))
    if amount_due < 0:
        print(
            f"Change Owed: {-amount_due}"
        )  # Display the positive value of change owed
    else:
        print("No change owed. Thank you!")


main()
