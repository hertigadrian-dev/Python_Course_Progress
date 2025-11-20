
import requests


url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin",
    "vs_currencies": "usd,eur,gbp"
    }

response = requests.get(url, params=params)
data = response.json()

print("Bitcoin Price:")
print(f"USD: ${data['bitcoin']['usd']}")
print(f"EUR: €{data['bitcoin']['eur']}")
print(f"GBP: £{data['bitcoin']['gbp']}")