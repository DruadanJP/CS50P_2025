def main():
    time = input("What time is it? ")
    if time.endswith("a.m."):
        time = convert(time)
        if 7 <= time <= 8:
                print("breakfast time")
        if 12 <= time <= 13:
                print ("lunch time")
    elif time.endswith("p.m."):
        time = convert(time)
        if 6 <= time <= 7:
                print("dinner time")
    
def convert(time):
    if "a.m." in time:
        time = time.replace("a.m.", "") # Remove "a.m."
    elif "p.m." in time:
        time = time.replace(" p.m.", "")  # Remove "p.m."
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    time = hours + minutes
    return time


if __name__ == "__main__":
    main()