# Hackerrank Language Proficiency Module: Python
# Title: sWAP cASE
# Directory: Python > Strings > sWAP cASE

import math
import os
import random
import re
import sys


def swap_case(s):
    reverse_string = ""
    for char in s:
        if char.isupper():
            reverse_string += char.lower()
        elif char.islower():
            reverse_string += char.upper()
        else:
            reverse_string += char

    return reverse_string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
