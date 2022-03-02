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
#  2. INTEGER m
#
# arr에 정수들이 오름차순으로 주어진다. 이 arr의 부분 집합 중 크기가 m인 집합들의 리스트를 X1, X2, X3,..,Xn 이라고 하자.
# 그리고 X라는 리스트에서 연속된 두 숫자의 차이 중 가장 작은 값을 S(X)라고 하자. 
# 이 때 S(X1), S(X2), S(X3), ... , S(Xn) 값 중 가장 큰 값을 구하시오.
#

def plus(x, nums, n):
    while x < n:
        if nums[x+1]:
            return x+1
        else: x += 1
    return n


def check(arr, k):
    n = len(arr)
    nums = [True]*n
    i = 0
    j = 1
    count = 0
    while j < n:
        if arr[j] - arr[i] < k:
            nums[j] = False
            count += 1
        else:
            i = plus(i, nums, n)    
        j += 1
    return count

def solution(arr, m):
    answer = 0
    n = len(arr)
    i = 1
    stop_2x = False
    high = 0
    low = 0
    while True:
        count = check(arr, i)
        print(i, count)
        if count <= n - m:
            answer = max(answer, i)
            if stop_2x:
                low = i
                i += max((high-low)//2, 1)
            else:
                i *= 2
        else:
            if stop_2x:
                if i - answer == 1:
                    break
                else:
                    high = i
                    i -= max((high-low)//2, 1) 
            else:
                high = i
                i //= 2
                low = i
                stop_2x = True
        print(high, low)
    return answer
        
        
'''
후기

'''