import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

API_KEY = os.getenv("API_KEY")
base = "USD"
# Here I am converting Dollars to Euros. Check the documentation to see what kind of rates you would need.
rates = "EUR"


oauth_url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}&base={base}&&symbols={rates}"

res = requests.get(url=oauth_url)


with open("token.json", "w") as f:
    f.write(json.dumps(res.json(), indent=4))

df = pd.DataFrame(res.json())
# df.info()
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
#soluction for the error given without "unit='s': https://stackoverflow.com/questions/51587468/datetime-defaulting-to-1970-in-pandas"


print(df)
print(df.dtypes)





