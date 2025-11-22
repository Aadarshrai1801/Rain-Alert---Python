import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
MY_NUMBER = os.getenv("MY_NUMBER")
FROM_NUMBER = os.getenv("FROM_NUMBER")

MY_LAT = 31.633980
MY_LNG = 74.872261

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": MY_LAT,
    "longitude": MY_LNG,
    "hourly": "precipitation_probability,precipitation"
}

response = requests.get(url, params=params)
data = response.json()

rain_expected = False

# Check next 12 hours
for i in range(12):
    rain_prob = data["hourly"]["precipitation_probability"][i]
    rain_amount = data["hourly"]["precipitation"][i]

    if rain_prob > 50 or rain_amount > 0:
        rain_expected = True
    
client = Client(account_sid, auth_token)    
        
if rain_expected :  
    message = client.messages.create (
    body = "It is going to rain today. Bring Your Umbrella",
    from_= FROM_NUMBER,
    to = MY_NUMBER, # type: ignore
    )
else :
    message = client.messages.create (
    body = "It is not going to rain today.",
    from_= FROM_NUMBER,
    to = MY_NUMBER,  # type: ignore
    )
         