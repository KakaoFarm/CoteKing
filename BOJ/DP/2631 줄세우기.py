from bisect import bisect_left
import sys

array = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    array.append(int(input()))

finder = []
for child in array:
    k = bisect_left(finder, child)
    if len(finder) <= k:
        finder.append(child)
    else:
        finder[k] = child

print(N - len(finder))