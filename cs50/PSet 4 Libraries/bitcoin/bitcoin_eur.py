import sys
import requests
import json

def bitcoin():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            count = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = response.json()
    bitcoin_price = response["bpi"]["EUR"]["rate_float"]
    amount = count * bitcoin_price
    print(f"€{amount:,.4f}")

bitcoin()
    