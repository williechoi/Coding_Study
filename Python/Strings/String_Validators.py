# Hackerrank Language Proficiency Module: Python
# Title: String Validators
# Directory: Python > Strings > String Validators

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()
    is_any_num = False
    is_any_alpha = False
    is_any_digit = False
    is_any_upper = False
    is_any_lower = False
    for let in range(0, len(s)):
        if s[let].isalnum():
            is_any_num = True
        if s[let].isalpha():
            is_any_alpha = True
        if s[let].isdigit():
            is_any_digit = True
        if s[let].isupper():
            is_any_upper = True
        if s[let].islower():
            is_any_lower = True

    print("{}\n{}\n{}\n{}\n{}".format(is_any_num, is_any_alpha, is_any_digit, is_any_lower, is_any_upper))
