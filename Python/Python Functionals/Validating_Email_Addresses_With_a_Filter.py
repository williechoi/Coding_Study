# Hackerrank Language Proficiency Module: Python
# Title: Validating Email Addresses With a Filter
# Directory: Python > Python Functionals > Validating Email Addresses With a Filter

import math
import os
import random
import re
import sys


# return True if s is a valid mail, else return False
def fun(s):
    if re.fullmatch("[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{1,3}", s):
        return True
    else:
        return False


# Filters emails based on the formula
def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)