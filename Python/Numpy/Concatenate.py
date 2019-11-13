# Hackerrank Language Proficiency Module: Python
# Title: Concatenate
# Directory: Python > Numpy > Concatenate

import math
import os
import random
import re
import sys
import numpy as np

if __name__ == "__main__":
    list1 = list()
    list2 = list()
    row_1, row_2, col = list(map(int, input().split()))
    for i in range(0, row_1):
        list1.append(list(map(int, input().split())))
    for j in range(0, row_2):
        list2.append(list(map(int, input().split())))
    array1 = np.array(list1)
    array2 = np.array(list2)
    print(np.concatenate((array1, array2), axis=0))
