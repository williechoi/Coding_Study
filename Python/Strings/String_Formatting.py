# Hackerrank Language Proficiency Module: Python
# Title: String Formatting
# Directory: Python > Strings > String Formatting

import math
import os
import random
import re
import sys


def print_formatted(number):
    for i in range(1, number+1):
        width = len("{:b}".format(number))
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
