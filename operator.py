#!/usr/bin/python -OOtt

# change these coordinates to match your location
lat = 38.8894541
lng = -77.0373655

from sunupdown import Sunupdown
from subprocess import Popen, PIPE
from time import sleep
import datetime
import sys

def door_up():
    p = Popen(cmd=['python','motor_sunrise.py'], stdout=PIPE, stderr=PIPE)
    p.communicate()

def door_down():
    p = Popen(cmd=['python','motor_sunset.py'], stdout=PIPE, stderr=PIPE)
    p.communicate()

######################################

# start with door down to initialize the state
sun = Sunupdown(lat,lng)
up,down = sun.fetch()
door_down()

if up > down:
    # door should be up right now
    door_up()
else:
    # door should stay down
    pass

try:
    # run forever
    while True:
        up,down = sun.fetch()
        print "Sleeping %s seconds until sunrise." % up
        sleep(up)

        print "Opening Door."
        door_up()

        up,down = sun.fetch()
        print "Sleeping %s seconds until sunset." % down
        sleep(down)

        print "Closing Door."
        door_down()

except Exception as e:
    # try complaining to syslog
    try:
        msg = '"Chicken Controller Operator Error: %s"' % e
        Popen(cmd=['logger',msg], stdout=PIPE, stderr=PIPE)
    except:
        pass

    sleep(1) # avoid thrashing
    sys.exit(1) # die in a fire
