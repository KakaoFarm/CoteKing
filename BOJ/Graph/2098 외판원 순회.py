N = int(input())
costs = []
for _ in range(N):
    cost_list = list(map(int, input().split()))
    for i in range(N):
        if cost_list[i] == 0:
            cost_list[i] = float('INF')
    costs.append(cost_list)

def isIn(i, A):
    if A & (1 << i) != 0:
        return True
    else:
        return False


def diff(A, j):
    return A & ~(1 << j)


def count(A):
    count = 0
    for i in range(N):
        if A & (1 << i) != 0:
            count += 1
    return count


def minimum(i, A):
    minValue = float('INF')
    for j in range(N):
        if isIn(j, A):
            cost = costs[i][j] + dp[j][diff(A, j)]
            minValue = min(minValue, cost)
    return minValue



dp = [[0]*(2**(N)) for _ in range(N)]
sets = [[] for _ in range(N+1)]
for i in range(1, N):
    dp[i][0] = costs[i][0]
for A in range(2**(N)):
    if not isIn(0, A):
        sets[count(A)].append(A)
for k in range(1, N-1):
    for A in sets[k]:
        for i in range(1, N):
            if not isIn(i, A):
                dp[i][A] = minimum(i, A)
A = (1<<N) - (1<<1)
print(minimum(0, A))
