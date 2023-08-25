#!/bin/python3

import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    database = "airports",
    user = "schooldb",
    password = "schooldb",
    autocommit = True
    )

def getAirport(airport):
    cursor = connection.cursor()
    query = ("SELECT name, municipality FROM airport WHERE ident = %s")
    cursor.execute(query, (str(airport), ))
    data = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in data:
            print(f"{row[0]}, {row[1]}")
    return

def main():
    icao = input("Anna ICAO koodi: ")
    getAirport(icao)

if __name__ == "__main__":
    main()
