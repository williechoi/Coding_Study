# Hackerrank Language Proficiency Module: Python
# Title: Map and Lambda Function
# Directory: Python > Python Functionals > Map and Lambda Function

import math
import os
import random
import re
import sys


cube = lambda x: x ** 3


def fibonacci(n):
    fibo_list = [0, 1]
    for i in range(2, n):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])

    return fibo_list[0:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))