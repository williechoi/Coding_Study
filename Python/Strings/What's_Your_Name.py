# Hackerrank Language Proficiency Module: Python
# Title: What's Your Name?
# Directory: Python > Strings > What's Your Name?

import math
import os
import random
import re
import sys


def print_full_name(a, b):
    print("Hello %s %s! You just delved into python." % (a, b))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)