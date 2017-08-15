#!/usr/bin/python -OOtt
# Print time until next sunrise and sunset in seconds

import requests
import datetime

lat,long = (22.1234567,-55.7654321)
url = "https://api.sunrise-sunset.org/json?lat=%s&lng=%s&date=today&formatted=0" % (lat, long)
#data = requests.get(url)
data = eval("""{"results":{"sunrise":"2017-08-15T11:49:56+00:00","sunset":"2017-08-16T01:02:08+00:00","solar_noon":"2017-08-15T18:26:02+00:00","day_length":47532,"civil_twilight_begin":"2017-08-15T11:24:58+00:00","civil_twilight_end":"2017-08-16T01:27:07+00:00","nautical_twilight_begin":"2017-08-15T10:55:13+00:00","nautical_twilight_end":"2017-08-16T01:56:52+00:00","astronomical_twilight_begin":"2017-08-15T10:24:28+00:00","astronomical_twilight_end":"2017-08-16T02:27:37+00:00"},"status":"OK"}""")

now = datetime.datetime.now()
utcnow = datetime.datetime.utcnow()
offset = (utcnow-now).seconds

sunrise = data['results']['sunrise'] # "2017-08-13T23:05:21+00:00"
sunset = data['results']['sunset']   # "2017-08-14T12:22:04+00:00"

# chop timezome because strptime doesnt seem to handle %z format.
sunrise = datetime.datetime.strptime(sunrise[:-6], "%Y-%m-%dT%H:%M:%S")
sunset = datetime.datetime.strptime(sunset[:-6], "%Y-%m-%dT%H:%M:%S")

sunrise = sunrise - datetime.timedelta(seconds=offset)
sunset = sunset - datetime.timedelta(seconds=offset)

# output number of seconds from now until sunrise and sunset
until_rise = (sunrise-now).seconds
until_set = (sunset-now).seconds

#print "Sunrise in %.2f hours." % (until_rise/60.0/60.0)
#print "Sunset in %.2f hours." % (until_set/60.0/60.0)
print until_rise, until_set
