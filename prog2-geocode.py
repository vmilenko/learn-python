#! /usr/bin/env python3

from geopy.geocoders import Nominatim

if __name__ == '__main__':
    print("This program prints geo coordinates of address")
    print("Enter address: ", end = "")
    address = input()
    user_agent = "General use for test in prog1-geocod.py"
    geolocator = Nominatim(user_agent=user_agent)

    location = geolocator.geocode(address)
    print("Geo Coordinates [Latitude | Longitude] -->")
    print(location.latitude, location.longitude)







