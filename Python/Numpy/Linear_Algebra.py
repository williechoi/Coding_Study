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
    matrix_a = list()
    N = int(input())
    for _ in range(N):
        matrix_a.append(list(map(float, input().split())))
    matrix_a = np.array(matrix_a)
    print(np.round(np.linalg.det(matrix_a), 2))
