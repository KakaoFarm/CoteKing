import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = [0]*(N+1)
tree = [0]*(N+1)

def GetPrefixSum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i)
    return result

def Update(i, diff):
    while i <= N:
        tree[i] += diff
        i += (i & -i)

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        b, c = min(b, c), max(b, c)
        answer = GetPrefixSum(c) - GetPrefixSum(b-1)
        sys.stdout.write(str(answer) + "\n")
    elif a == 1:
        Update(b, c - nums[b])
        nums[b] = c
