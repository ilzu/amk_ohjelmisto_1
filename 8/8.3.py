#!/bin/python3

import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    database = "airports",
    user = "schooldb",
    password = "schooldb",
    autocommit = True
    )

def getDistance(source, destination):
    src = None
    dest = None
    cursor = connection.cursor()
    query = ("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s LIMIT 1")
    cursor.execute(query, (str(source),))
    data = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in data:
            src = (row[0], row[1])
    cursor.execute(query, (str(destination),))
    data = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in data:
            dest = (row[0], row[1])
    
    print(f"Välimatka kenttien {source} ja {destination} välillä on {distance.distance(src,dest).km} kilometriä.")
    return

def main():
    source  = input("Anna lähtöpisteen ICAO koodi: ")
    destination = input("Anna kohdepisteen ICAO koodi: ")
    getDistance(source, destination)

if __name__ == "__main__":
    main()
