#!/bin/python3

import requests
import json

def main():
    try:
        reply = requests.get("https://api.chucknorris.io/jokes/random").json()
        print(reply["value"])

    except requests.exceptions.RequestException as e:
        print(f"Haku ei onnistunut {e}")
    
if __name__ == "__main__":
    main()
