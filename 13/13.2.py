#!/bin/python3

import mysql.connector
from flask import Flask

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    database = "airports",
    user = "schooldb",
    password = "schooldb",
    autocommit = True
    )

app = Flask(__name__)

@app.route('/kenttä/<icao>')
def getAirport(icao):
    cursor = connection.cursor()
    query = ("SELECT name, municipality FROM airport WHERE ident = %s")
    cursor.execute(query, (str(icao), ))
    data = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in data:
            reply = { 
                "ICAO" : icao,
                "Name" : row[0], 
                "Mucipality": row[1]
                }
            return reply
    return {"Error:": "Invalid ICAO"}


if __name__ == "__main__":
    app.run(use_reloader = True, host = 'localhost', port = 3000)
