# Hackerrank Language Proficiency Module: Python
# Title: Python If-Else
# Directory: Python > Introduction > Python If-Else

import math
import os
import random
import re
import sys


if __name__ == "__main__":
    n = int(input().strip())
    if n % 2 is not 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
