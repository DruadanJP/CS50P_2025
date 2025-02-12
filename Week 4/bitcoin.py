import requests
import json
import sys

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Not a number")
        sys.exit(1)
else:
    print("Missing Command Line Argument")
    sys.exit(1)


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = response.json()
    bitcoin = response["bpi"]["USD"]["rate_float"]
    total_amount = bitcoin * value
    print(total_amount)
    print(f"${total_amount:,.4f}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
    sys.exit(1)