#! /usr/bin/env python3
# author: Daniel Montes TODO: YOUR NAME

from json import loads
from requests import get
from socket import gethostbyname
from subprocess import getstatusoutput
from sys import argv


# Retrieve IP from the domain
def get_IP(domain_name):
    try:
        ip_address = gethostbyname(domain_name)
        print(ip_address)
        return ip_address
    except Exception as d:
        print(f"Failure to resolve IP address for {domain_name}: {d}")
        return None

    # Get physical address
def getAddress(ip_address):
    whois_cmd = f"whois {ip_address}"
    status, output = getstatusoutput(whois_cmd)

    if status != 0:
        print(f"Failed to execute whois command for IP address {ip_address}")
        return None, None, None, None

    # Print the WHOIS command output
    print(f"WHOIS output for IP {ip_address}:")
    ##print(output)

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

    # Print the address: street, city, and state, zipcode
    print(f"Address: {street}, City: {city}, State: {state}, Postal Code: {postalcode}")

    return street, city, state, postalcode


# Retrieve the coordinates
def get_coordinates(street, city, state, postalcode):
    geocode_url = "https://geocoding.geo.census.gov/geocoder/locations/address?"
    geocode_address = "street=" + street + "&city=" + city + "&state=" + state + "&zip=" + postalcode
    gecode_end = "&benchmark=Public_AR_Census2020&format=json"
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
    print("No address has been found.")
    return None, None


# Retrieve Latitude & Longitude using the URL
def get_weather(latitude, longitude):
    weather_url = f"https://api.weather.gov/points/{latitude},{longitude}"

    response = get(weather_url)

    # If fails to retrieve coordinates
    if response.status_code != 200:
        print(f"Failure to retrieve weather data for coordinates: {latitude}, {longitude}")
        return None

    data = loads(response.text)
    forecast_url = data["properties"]["forecast"]

    forecast_response = get(forecast_url)

    # Print statement for failed retrival of data
    if forecast_response.status_code != 200:
        print(f"Failure to retrieve forecast data from the URL: {forecast_url}")
        return None

    forecast_data = loads(forecast_response.text)
    detailed_forecast = forecast_data["properties"]["periods"][0]["detailedForecast"]

    return detailed_forecast


def main():
    if len(argv) != 2:
        print("Correct use is python3 lab2.py <domain_name>")
        return

    domain_name = argv[1]

    ip_address = get_IP(domain_name)
    if not ip_address:
        return

    # Print statement if address is not retrieved
    street, city, state, postalcode = getAddress(ip_address)
    if not street or not city or not state or not postalcode:
        print("Failed to retrieve the physical address.")
        return

    longitude, latitude = get_coordinates(street, city, state, postalcode)
    if not longitude or not latitude:
        return

    # Forecast print statement
    detailed_forecast = get_weather(latitude, longitude)
    if detailed_forecast:
        print(f"Forecast for {domain_name} (Location: {latitude}, {longitude}):")
        print(detailed_forecast)


if __name__ == "__main__":
    main()
