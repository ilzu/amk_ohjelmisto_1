#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/alkuluku/<num>')
def isPrime(num):
    num = int(num)
    prime = True
    for i in range(2, num // 2):
        if num % i == 0 and i != num:
            prime = False
            break
    reply = {
        "number" : num,
        "isPrime" : prime
        }
    return reply

if __name__ == "__main__":
    app.run(use_reloader = True, host = 'localhost', port = 3000)

