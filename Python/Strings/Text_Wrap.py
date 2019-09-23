# Hackerrank Language Proficiency Module: Python
# Title: Text Wrap
# Directory: Python > Strings > Text Wrap

import math
import os
import random
import re
import sys

import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
