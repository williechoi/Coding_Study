# Hackerrank Language Proficiency Module: Python
# Title: Mutations
# Directory: Python > Strings > Mutations

import math
import os
import random
import re
import sys


def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
