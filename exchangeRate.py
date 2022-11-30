import requests
from dotenv import load_dotenv
import os
load_dotenv()
private_key = os.getenv("PRIVATE_KEY")

# url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=EUR&amount=50"
url = "https://api.apilayer.com/exchangerates_data/latest?symbols=EUR,AUD,AZN,GBP&base=USD"

payload = {}
headers= {
  "apikey": private_key
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
print(status_code)
result = response.text
print(result)