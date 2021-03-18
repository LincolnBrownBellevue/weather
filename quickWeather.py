#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys, pprint

#Compute location from command line arguments.
zip = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = 'https://api.openweathermap.org/data/2.5/weather?zip=%s&appid=29b0bae73452e939b5e9067b947a3da5' % (zip)

response = requests.get(url)

# Load JSON data into a Python variable
weatherData = json.loads(response.text)
response.raise_for_status()

# Print weather descriptions.
# w = weatherData['list']
city =  weatherData['name']
print('Current weather in %s:' % (city))
current = weatherData['weather']
temp = weatherData['main']['temp']
tempF = int(1.8*(temp-273) + 32)
print('Temperature is %s' % (tempF))
print(current[0]['main'] + " - " + current[0]['description'])
