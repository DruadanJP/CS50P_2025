grocery = []

while True:
    try:
        item = input("").upper()
        grocery.append(item)  # Add the item to the grocery list
    except EOFError:  # When input ends
        unique_items = sorted(set(grocery))  # Get unique items in sorted order
        for unique_item in unique_items:
            print(grocery.count(unique_item), unique_item)  # Print count and item
        break
