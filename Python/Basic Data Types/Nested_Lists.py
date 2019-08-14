# Hackerrank Language Proficiency Module: Python
# Title: Nested Lists
# Directory: Python > Basic Data Types > Nested Lists

import math
import os
import random
import re
import sys

marksheet = []
scorelist = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet += [[name, score]]
        scorelist += [score]

    scorelist = list(dict.fromkeys(scorelist))
    b = sorted(scorelist)[1]

    for a, c in sorted(marksheet):
        if c == b:
            print(a)

