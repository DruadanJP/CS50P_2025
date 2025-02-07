def main():
    User = {"name": "Yuka "}   
    User.update({"Surname": "Yamamoto", "Country": "Japan"})
    print(create_report(User))
    
def create_report(User):
    return f"""
    ===REPORT===
    Name: {User.get("name", "Unknown")}
    Surname: {User.get("Surname", "Unknown")} 
    Country: {User.get("Country", "Unknown")} 
    ========="""
   
main()