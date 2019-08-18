# Hackerrank Language Proficiency Module: Python
# Title: String Split and Join
# Directory: Python > Strings > String Split and Join

import math
import os
import random
import re
import sys


def split_and_join(line):
    return '-'.join(line.split(' '))


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
