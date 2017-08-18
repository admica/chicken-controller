#!/usr/bin/python -OOtt
# Fetch time until next sunrise and sunset in seconds

import requests
import datetime

class Sunupdown(object):

    def __init__(self, lat=38.8895461, lng=-77.0361769):
        self.lat = lat
        self.lng = lng
        self.url = "https://api.sunrise-sunset.org/json?lat=%s&lng=%s&date=today&formatted=0" % (self.lat, self.long)

        self.online = False # last lookup was successful
        self.last_rise = None # first lookup will set this
        self.last_set = None # first lookup will set this

        self.until_rise = 1
        self.until_set = 1

        now = datetime.datetime.now()
        utcnow = datetime.datetime.utcnow()
        self.offset = (utcnow-now).seconds


    def fetch(self):
        """calculate time until next sunrise and sunset"""
        try:
            data = requests.get(self.url)
            data = data.response()

            sunrise = data['results']['sunrise'] # string date
            sunset = data['results']['sunset'] # string date

            # chop timezome because strptime doesnt seem to handle %z format.
            sunrise = datetime.datetime.strptime(sunrise[:-6], "%Y-%m-%dT%H:%M:%S")
            sunset = datetime.datetime.strptime(sunset[:-6], "%Y-%m-%dT%H:%M:%S")

            sunrise = sunrise - datetime.timedelta(seconds=self.offset)
            sunset = sunset - datetime.timedelta(seconds=self.offset)
            self.online = True

        except:
            sunrise = self.last_rise + datetime.timedelta(seconds=86400) # add 24 hours
            sunset = self.last_set + datetime.timedelta(seconds=86400)

            self.last_rise = sunrise
            self.last_set = sunset
            self.online = False

        # output number of seconds from now until sunrise and sunset
        now = datetime.datetime.now()
        self.until_rise = (sunrise-now).seconds
        self.until_set = (sunset-now).seconds

        return (self.until_rise, self.until_set)


    def __str__(self):
        """pretty print"""
        return "Sunrise in %.2f hours, Sunset in %.2f hours." % (self.until_rise/60.0/60.0, self.until_set/60.0/60.0)


if __name__ == '__main__':

    sun = Sunupdown(lat=8.8895461, lng=-77.0361769)
    up, down = sun.fetch()

    print "Timezone offset from UTC:", sun.offset
    print "Up/Down in seconds:", up, down
    print sun

