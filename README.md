# PiTwitterCamera
## Functionality
This is a surveillance camera system scripted in Python. It detects and records movements. The recordings are saved locally, movements are reported to Twitter using tweepy.
## Requirements
För att utföra detta projekt bör du ha dessa.
#### Hardware
* Raspberry Pi
* Raspberry Pi camera module
* PIR Motion Sensor
* Tactile button
* Quick-connect wires
#### Software
* Python 3
* pip
#### Python Modules
* gpiozero
* picamera
* datetime
* signal
* json
* tweepy

You also need to own a Twitter developer account.

##Circuit
![Circuit](/Circuit.png "Circuit")
PIN layout: https://gpiozero.readthedocs.io/en/stable/_images/pin_layout.svg.
The camera module has to be connected as well.
