#! /usr/bin/env python3
# author: Daniel Montes

from flask import Flask
from json import loads
from requests import get
from socket import gethostbyname
from subprocess import getstatusoutput


app = Flask(__name__)

cache = {}
cache2 = {}

def get_address(domain_name):
    # Check if the user's entry is already cached
    if domain_name in cache:
        print(f"Cached: {cache[domain_name]}")

    ip_address = get_IP(domain_name)
    if not ip_address:
        print(f"Failure to resolve IP address for {domain_name}")

    physical_address = getAddress(ip_address)
    if not physical_address:
        print(f"Failure to retrieve physical address.")

    # Cache user's entry
    cache[domain_name] = physical_address

    return str(physical_address)

@app.route("/weather/<domain_name>")
def get_weatherData(domain_name):
    # Check if the response is already cached
    if domain_name in cache2 and domain_name is not None:
        return "cached: " + cache2[domain_name]

    ip_address = get_IP(domain_name)
    if not ip_address:
        print(f"Failure to resolve IP address for {domain_name}")

    physical_address = getAddress(domain_name)
    if not physical_address:
        print(f"Failure to retrieve the physical address.")

    latitude, longitude = get_coordinates(*physical_address[:4])
    if not latitude or not longitude:
        print(f"Failure to retrieve the coordinates(LAT/LONG).")

    weather_info = get_weather(latitude, longitude)
    if not weather_info:
        print(f"Failure to retrieve weather data.")

    # Cache the response
    cache2[domain_name] = weather_info

    return weather_info

# Retrieve Latitude & Longitude using the URL
def get_weather(latitude, longitude):
    weather_url = f"https://api.weather.gov/points/{longitude},{latitude}"

    response = get(weather_url)

    data = loads(response.text)
    forecast_url = data["properties"]["forecast"]

    forecast_response = get(forecast_url)

    # Print statement for failed retrieval of data
    if forecast_response.status_code != 200:
        print(f"Failure to retrieve forecast data from the URL: {forecast_url}")
        return None

    forecast_data = loads(forecast_response.text)
    detailed_forecast = forecast_data["properties"]["periods"][0]["detailedForecast"]

    return detailed_forecast

# Get physical address
def getAddress(domain_name):
    ip_address = get_IP(domain_name)
    whois_cmd = f"whois {ip_address}"
    status, output = getstatusoutput(whois_cmd)

    if status != 0:
        print(f"Failure to execute whois command for IP address {ip_address}")
        return None, None, None, None


    # Parse the WHOIS output to find the physical address
    lines = output.splitlines()
    street = None
    city = None
    state = None
    postalcode = None

    # Loop through each line in the WHOIS output
    for line in lines:
        line_lower = line.lower()

        if "address:" in line_lower:
            # Get the street
            street = line.split(":", 1)[1].strip()
        elif "city:" in line_lower:
            # Get the city
            city = line.split(":", 1)[1].strip()
        elif "state:" in line_lower or "stateprov:" in line_lower:
            # Get the state
            state = line.split(":", 1)[1].strip()
        elif "postalcode:" in line_lower:
            postalcode = line.split(":", 1)[1].strip()

    # Print the address: street, city, state, zipcode
    print(f"Address: {street}, City: {city}, State: {state}, Postal Code: {postalcode}")

    return street, city, state, postalcode


# Retrieve the coordinates
def get_coordinates(street, city, state, postalcode):
    geocode_url = "https://geocoding.geo.census.gov/geocoder/locations/address?"
    geocode_address = "street=" + street + "&city=" + city + "&state=" + state + "&zip=" + postalcode
    gecode_end = "&benchmark=Public_AR_Current&format=json"
    gecode_full = geocode_url + geocode_address + gecode_end
    params = {
        "street": street,
        "city": city,
        "state": state,
        "postalcode": postalcode,
        "benchmark": "Public_AR_Census2020",
        "format": "json"
    }

    response = get(geocode_url, params=params)

    # Failure to retrieve coordinates for {street}, {city}, {state}, {postalcode}
    if response.status_code != 200:
        print(f"Failure to retrieve coordinates for the address: {street}, {city}, {state}, {postalcode}")
        return None, None

    data = loads(response.text)

    if data.get("result") and data["result"].get("addressMatches"):
        coordinates = data["result"]["addressMatches"][0]["coordinates"]
        return coordinates["x"], coordinates["y"]

    # If address cannot be found it'll print
    print(f"No address has been found.")
    return None, None

    # Retrieve IP address
def get_IP(domain_name):
    try:
        ip_address = gethostbyname(domain_name)
        return ip_address
    except Exception as d:
        print(f"Failure to resolve IP address for {domain_name}: {d}")
        return None

@app.route("/upper/<echo_string>")
def upper(echo_string):
    return echo_string.upper()

@app.route("/address/<domain_name>")
def address(domain_name):
    if domain_name in cache:
        return "cached:" + cache[domain_name]
    address, city, state, postal = getAddress(domain_name)
    location = address + ', ' + city + ', ' + state + ', ' + postal
    cache[domain_name] = location
    return location

@app.route("/callwhois")
def whois():
    status, output = getstatusoutput("whois 8.8.8.8")
    return output


@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()