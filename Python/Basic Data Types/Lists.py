# Hackerrank Language Proficiency Module: Python
# Title: Lists
# Directory: Python > Basic Data Types > Lists

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    answer_list = list()
    for _ in range(N):
        command = input().split(' ')
        order = command[0]
        if order == 'insert':
            answer_list.insert(int(command[1]), int(command[2]))
        elif order == 'remove':
            answer_list.remove(int(command[1]))
        elif order == 'append':
            answer_list.append(int(command[1]))
        elif order == 'pop':
            answer_list.pop()
        elif order == 'reverse':
            answer_list.reverse()
        elif order == 'sort':
            answer_list.sort()
        elif order == 'print':
            print(answer_list)
