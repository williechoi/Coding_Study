# Hackerrank Language Proficiency Module: Python
# Title: Arrays
# Directory: Python > Numpy > Arrays

import math
import os
import random
import re
import sys
import numpy as np

def arrays(arr):
    return np.array(arr[::-1], float)


if __name__ == "__main__":
    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)

