months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
        date = input("Date: ")

        # Reject mixed formats (e.g., "October/9/1701")
        if any(month in date for month in months) and "/" in date:
            continue

# Validate numeric dates (e.g., "9/8/1636")
        if "/" in date:
            month, day, year = date.split("/")
            if month.isalpha():
                continue
            else:
                month = int(month)
                day = int(day)
                year = int(year)
            try:
                if not (1 <= month <= 12) or not (1 <= day <= 31):
                    continue
                print(f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}")
                break
            except ValueError:
                break
                
# Validate written dates (e.g., "September 8, 1636")
        elif " " in date:
            if "," not in date:
                continue
            try:
                parts = date.replace(",", "").split(" ")
                month, day, year = parts[0], parts[1], parts[2]
                if month.isdigit():
                    continue
                month = months.index(month) + 1
                day = int(day)  # Ensure day is numeric
                if not (1 <= day <= 31):
                    continue  # Skip invalid days
                print(f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}")
                break
            except(ValueError, IndexError):
                continue
