#!/usr/bin/python -OOtt

import yaml
config = yaml.load(open('config.txt','r'))
lat = config['latitude']
lng = config['longitude']

import zmq
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:1234")

from sunupdown import Sunupdown
from subprocess import Popen, PIPE
from time import sleep
import datetime

def door_up():
    p = Popen('python motor_sunrise.py', shell=True, stdout=PIPE, stderr=PIPE)
    p.communicate()

def door_down():
    p = Popen('python motor_sunset.py', shell=True, stdout=PIPE, stderr=PIPE)
    p.communicate()

def outp(msg):
    print msg
    try:
        socket.send(msg)
    except:
        pass

######################################

# run forever
while True:

    try:
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

        while True:
            up,down = sun.fetch()
            outp("Sleeping %s seconds until sunrise." % up)
            sleep(up)

            outp("Opening Door.")
            door_up()

            up,down = sun.fetch()
            outp("Sleeping %s seconds until sunset." % down)
            sleep(down)

            outp("Closing Door.")
            door_down()

    except Exception as e:
        # try complaining to syslog
        try:
            msg = '"Chicken Controller Operator Error: %s"' % e
            cmd = 'logger %s' % msg
            Popen(cmd, stdout=PIPE, stderr=PIPE)
        except:
            pass

        sleep(30) # avoid thrashing before falling back to outer loop...

