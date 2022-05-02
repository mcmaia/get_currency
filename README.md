# Get Currency

Sign up to `<https://openexchangerates.org/>` so you can get your APP ID.

It is a goog idea to go to the ENDPOINTS and read the examples

## To hide your API KEYS

Create a archive .env (see main.py).

## To create a virtual environment
In your prmpt:

```python
python -m venv venv
```
## Start the virtual evironment

```for windows
source venv/Script/activate
```

```python
pip install python-dotenv
```

### Do not forget to install all the instances you are importing in the virtual environment.

# Explaining the code:
```python
import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd
```
First, I imported all the libraries I was going to use. 

```python
API_KEY = os.getenv("API_KEY")
base = "USD"
# Here I am converting Dollars to Euros. Check the documentation to see what kind of rates you would need.
rates = "EUR"


oauth_url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}&base={base}&&symbols={rates}"

res = requests.get(url=oauth_url)
```
Then, I created some variables to use in the URL. After that, I made a GET request to this URL.

```python
with open("token.json", "w") as f:
    f.write(json.dumps(res.json(), indent=4))

```
Afterwards, I created a json file to display the response.

```python
df = pd.DataFrame(res.json())
# df.info()
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
#soluction for the error given without "unit='s': https://stackoverflow.com/questions/51587468/datetime-defaulting-to-1970-in-pandas"


print(df)
print(df.dtypes)
```

Lastly, I created a dataframe, changed the timestemp to the human view and printed the result in the terminal.
