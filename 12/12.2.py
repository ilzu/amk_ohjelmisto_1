#!/bin/python3

import requests
import json
import sys

apikey = ""

def getCoordinates(locality):
    global apikey
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={locality}&limit=1&appid={apikey:.32}"

    try:
        reply = requests.get(url).json()
        lat = float(reply[0]["lat"])
        lon = float(reply[0]["lon"])
        return (lat, lon)
    except requests.RequestException as e:
        print(f"Haku ei onnistunut {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Virhe: {e}")


def getWeather(coordinates):
    global apikey
    try:

        url = f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates[0]}&lon={coordinates[1]}&units=metric&appid={apikey:.32}"
        reply = requests.get(url).json()
        summary = reply["weather"][0]["description"]
        temp = reply["main"]["temp"]
        print(f"Säätila: {summary} Lämpötila: {temp} celsiusastetta.")

    except requests.exceptions.RequestException as e:
        print(f"Haku ei onnistunut {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Virhe: {e}")
   
def main():
    try:
        f = open("./owapikey.txt", "r")
    except Exception as e:
        print("API key not found in owapikey.txt -file")
        sys.exit(1)

    global apikey
    apikey = f.readline()
    locality = input("Anna paikkakunta: ")
    coords = getCoordinates(locality)
    getWeather(coords)

if __name__ == "__main__":
    main()
