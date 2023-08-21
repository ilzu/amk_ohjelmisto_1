#!/bin/python3

import random

code1=""
code2=""

for i in range(3):
    code1 = code1 + str(random.randint(0, 9))

for i in range(4):
    code2 = code2 + str(random.randint(1, 6))

print("Koodi 1 = " + code1 + " koodi 2 = " + code2)

