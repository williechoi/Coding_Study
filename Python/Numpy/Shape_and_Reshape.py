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
    arr = np.array(list(map(int, input().split())))
    arr.shape = (3, 3)
    print(arr)

    arr2 = np.array(list(map(int, input().split())))
    print(np.reshape(arr2, (3, 3)))



