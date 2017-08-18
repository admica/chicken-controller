#!/usr/bin/python -OOtt

import yaml
config = yaml.load(open('config.txt','r'))
RUNTIME = config['motor_down_seconds']

PINA = 31
PINB = 33
PINC = 35
PIND = 37

# GPIO pinout for Raspberry Pi Model B+, Pi 2B, Pi Zero and Pi 3B:
#
# 5.0v 5.0v GRND gpio gpio gpio GRND gpio gpio GRND gpio gpio gpio idsc GRND gpio GRND gpio gpio gpio
# ---------------------------------------------------------------------------------------------------
# 2    4    6    8    10   12   14   16   18   20   22   24   26   28   30   32   34   46   38   40
# 1    3    5    7    9    11   13   15   17   19   21   23   25   27   29   31   33   35   37   39
# ---------------------------------------------------------------------------------------------------
# 3.3v gpio gpio gpio GRND gpio gpio gpio 3.3v gpio gpio gpio GRND idsd gpio gpio gpio gpio gpio GRND

import RPi.GPIO as GPIO
from time import sleep

# setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(PINA, GPIO.OUT)
GPIO.setup(PINB, GPIO.OUT)
GPIO.setup(PINC, GPIO.OUT)
GPIO.setup(PIND, GPIO.OUT)
GPIO.output(PINA, True)
GPIO.output(PINB, True)
GPIO.output(PINC, True)
GPIO.output(PIND, True)
sleep(.25)

# Turn on motor
GPIO.output(PIND, False)
GPIO.output(PINC, False)

sleep(RUNTIME)

# Turn off motor
GPIO.output(PINC, True)
GPIO.output(PIND, True)

