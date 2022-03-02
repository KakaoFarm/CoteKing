#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER x
#
# arr에 음이 아닌 정수들이 있고, 각 숫자들을 0보다 작아지지 않는 선에서 x만큼씩 빼거나 더할 수 있다.
# arr 내에서 가장 작은 숫자가 최대한 크도록 조작했을 때, 그 가장 작은 숫자를 구하시오.
#

def solution(arr, x):
    remainders = [0]*x
    for num in arr:
        k = num % x
        remainders[k] += 1
    
    INF = float('INF')
    min_value = INF
    min_index = 0
    for i in range(x):
        if remainders[i] < min_value:
            min_value = remainders[i]
            min_index = i
    
    answer = min_value * x + min_index
    return answer


'''
후기

'''