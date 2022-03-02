#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stockPrices
#  2. INTEGER k
#
# stockPices에 월별 판매수익이 주어졌을 때, k달 연속 수익이 상승한 구간의 수를 구하시오.
#

from collections import deque

def solution(stockPrices, k):
    answer = 0
    n = len(stockPrices)
    queue = deque()
    temp = 0
    for i in range(k-1):
        if stockPrices[i] < stockPrices[i+1]:
            queue.append(1)
            temp += 1
        else: queue.append(0)
    if temp == k-1:
        answer += 1
    for i in range(k-1, n-1):
        temp -= queue.popleft()
        if stockPrices[i] < stockPrices[i+1]:
            queue.append(1)
            temp += 1
        else: queue.append(0)
        if temp == k-1:
            answer += 1
    return answer


'''
후기

'''