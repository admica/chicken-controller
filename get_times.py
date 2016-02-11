#!/usr/bin/python -OOtt

import requests
from datetime import datetime

lat,long = (22.1234567,-55.7654321)
url = "https://api.sunrise-sunset.org/json?lat=%s&lng=%s&date=today&formatted=0" % (lat, long)
data = requests.get(url)

sunrise = data['results']['sunrise'] # "2017-08-13T23:05:21+00:00"
sunset = data['results']['sunset']   # "2017-08-14T12:22:04+00:00"

# need to handle timezone issue
sunrise = sunrise[:-6]
sunrise = datetime.strptime(sunrise, "%Y-%m-%dT%H:%M:%S")

now = datetime.now()

# output number of seconds from now until sunrise and sunset
print (sunrise-now).seconds,(sunset-now).seconds
