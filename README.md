# chicken-controller
Automatically open and close a chicken coop door at sunrise and sunset using a Raspberry Pi.

 * Git tree:  https://github.com/admica/chicken-controller.git
    * Clone with `git clone https://github.com/admica/chicken-controller.git`

#### Requirements
* python2
* python-requests (https://pypi.python.org/pypi/requests)
* RPi.GPIO (https://pypi.python.org/pypi/RPi.GPIO)

#### Files
- get_times.py -- fetches sunrise and sunset times from the internet for a given lat/long.
- motor_sunrise.py -- opens the door
- motor_sunset.py -- closes the door

#### Coordinates
The longitude/latitude used is the Washington Monument at 2 15th St NW, Washington, DC 20024

To get your location in lat/long, look up your address on google maps and find the values in the URL.

For example:
`https://www.google.com/maps/place/Washington+Monument/@38.8894541,-77.0373655`

