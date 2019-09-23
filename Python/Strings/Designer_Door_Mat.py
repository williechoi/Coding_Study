# Hackerrank Language Proficiency Module: Python
# Title: Designer Door mat
# Directory: Python > Strings > Designer Door Mat

import math
import os
import random
import re
import sys

PATTERN = ".|."


def doormat_creator(height, width):
    for i in range(1, height+1):
        if i < height//2 + 1:
            print((PATTERN*(2*i-1)).center(width, '-'))
        elif i == height//2 + 1:
            print("WELCOME".center(width, '-'))
        else:
            print((PATTERN*(2*(height-i)+1)).center(width, '-'))


if __name__ == "__main__":
    height, width = list(map(int, input().split()))
    doormat_creator(height, width)
    print("width is: {}".format(width))
    print("height is: {}".format(height))
