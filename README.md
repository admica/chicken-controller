# chicken-controller
Automatically open and close a chicken coop door at sunrise and sunset using a Raspberry Pi.

 * Git tree:  https://github.com/admica/chicken-controller.git
    * Clone with `git clone https://github.com/admica/chicken-controller.git`

 ### The only customizations you should need is to update operator.py with your own longitude/latitude and pin numbers for your gpio.
 ### Drop all files together anywhere you want, then update rc.local to reflect your path.
 ### Test motor up/down scripts to ensure your wiring is correct.
 ### Make sure rc.local loads at startup.

#### Requirements
* python2
* python-requests (https://pypi.python.org/pypi/requests)
* RPi.GPIO (https://pypi.python.org/pypi/RPi.GPIO)

#### Files
- operator.py -- Main app. Everything else is used internally by this program.
- sunupdown.py -- class Sunupdown fetches sunrise and sunset times from the internet for a given lat/long.
- motor_sunrise.py -- Turns on relay #1 and #2 to open the door
- motor_sunset.py -- Turns on relay #3 and #4 to close the door

#### Coordinates
The longitude/latitude used is the Washington Monument at 2 15th St NW, Washington, DC 20024

To get your location, look up your address on google maps in a browser and find the values in the URL.
* Example:
`https://www.google.com/maps/place/Washington+Monument/@38.8894541,-77.0373655`

