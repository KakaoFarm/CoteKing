import sys

sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
is_visited = [False for _ in range(N+1)]
dp = [[0,0] for _ in range(N+1)]
for _ in range(N-1):
    i, j = map(int,sys.stdin.readline().rstrip().split())
    graph[i].append(j)
    graph[j].append(i)

def solution(node):
    is_visited[node] = True
    dp[node][1] = 1
    for child in graph[node]:
        if is_visited[child] == False:
            solution(child)
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])

solution(1)
print(min(dp[1][0], dp[1][1]))