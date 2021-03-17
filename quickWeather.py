#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys

#Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join*sys.argv[1:])

#TODO: Download the JSON data from OpenWeatherMap.org's API.

#TODO Load JSON data into a Python variable

