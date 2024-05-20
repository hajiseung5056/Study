import requests

btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

print(btc)

min = int(btc["min_price"])
max = int(btc["max_price"])


변동폭 = max-min

if int(btc["max_price"]) < (int(btc["opening_price"]) + 변동폭):
    print("up")
else:
    print("down")
