# Hackerrank Language Proficiency Module: Python
# Title: Finding the percentage
# Directory: Python > Basic Data Types > Finding the percentage

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg_scr = 0
    score = student_marks.get(query_name)
    if score is not None:
        for i in range(0, len(score)):
            avg_scr += score[i]
        avg_scr = avg_scr / len(score)
        print("%.2f" % avg_scr)
    else:
        print("Query name does not exist")


