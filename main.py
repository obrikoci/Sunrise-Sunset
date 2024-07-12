import requests

# SUNRISE AND SUSNET
from datetime import datetime

MY_LAT = 47.327845
MY_LNG = 13.812699

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunrise_hour = sunrise.split("T")[1].split(":")[0]
print(sunrise_hour)
sunset_hour = sunset.split("T")[1].split(":")[0]
print(sunset_hour)

time_now = datetime.now()
print(time_now.hour)
