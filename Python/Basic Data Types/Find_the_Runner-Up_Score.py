# Hackerrank Language Proficiency Module: Python
# Title: List Comprehensions
# Directory: Python > Basic Data Types > List Comprehensions

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    largest_num = max(arr)
    print(largest_num)

    for i in range(0, len(arr)-1):
        print(arr[i])
        if arr[i] == largest_num:
            arr.remove(arr[i])

    print(arr)
    print(max(arr))
