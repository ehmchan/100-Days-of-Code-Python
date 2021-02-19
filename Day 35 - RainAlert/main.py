import requests
from twilio.rest import Client
import config

MY_LAT = 51.048615 # Your latitude
MY_LONG = -114.070847 # Your longitude
api_key = config.OWM_api_key
account_sid = config.twilio_account_sid
auth_token = config.twilio_auth_token

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_=config.twilio_phone_num,
        to=config.my_phone_num
    )

    print(message.status)
