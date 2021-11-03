from bisect import bisect_left
import sys

N = int(input())
arr = list(map(int, input().split()))

dp = [dict() for _ in range(N+1)]
temp = []
L = 0



for num in arr:
    k = bisect_left(temp, num)
    if k == L:
        temp.append(num)
        L += 1
    else:
        if temp[k] == num:
            continue
        temp[k] = num
    if k >= 1:
        dp[k+1][num] = temp[k-1]

print(L)
num = temp[L-1]
answer = []
answer.append(num)
for i in range(L, 1, -1):
    num = dp[i][num]
    answer.append(num)

for _ in range(L):
    sys.stdout.write(str(answer.pop()) + " ")
