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

def getAirports(country):
    cursor = connection.cursor()
    query = ("SELECT type, COUNT(type) as amount  FROM airport WHERE iso_country = %s GROUP BY type")
    cursor.execute(query, (str(country), ))
    data = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in data:
            print(f"{row[0]}, {row[1]}")
    return

def main():
    country = input("Anna maakoodi: ")
    getAirports(country)

if __name__ == "__main__":
    main()
