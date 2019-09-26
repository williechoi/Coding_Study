# Hackerrank Language Proficiency Module: Python
# Title: Shape and Reshape
# Directory: Python > Numpy > Shape and Reshape

import math
import os
import random
import re
import sys
import numpy as np

if __name__ == "__main__":
    array1 = list()
    N, M = tuple(map(int, input().split()))
    for _ in range(N):
        array1.append(list(map(int, input().split())))
    array1 = np.array(array1)
    print(np.transpose(array1))
    print(array1.flatten())
