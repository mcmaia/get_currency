import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
base = "USD"
# Here I am converting Dollars to Euros. Check the documentation to see what kind of rates you would need.
rates = "EUR"


oauth_url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}&base={base}&&symbols={rates}"

res = requests.get(url=oauth_url)

with open("token.json", "w") as f:
    f.write(json.dumps(res.json(), indent=4))
