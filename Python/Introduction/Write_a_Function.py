# Hackerrank Language Proficiency Module: Python
# Title: Write a function
# Directory: Python > Introduction > Write a function

import math
import os
import random
import re
import sys


def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True

    return leap


year = int(input())
print(is_leap(year))