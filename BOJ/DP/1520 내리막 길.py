N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[-1]*M for _ in range(N)]
dp[0][0] = 1

def get_routes(graph, x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return 0
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[x][y] < graph[nx][ny]:
            dp[x][y] += get_routes(graph, nx, ny)
    return dp[x][y]

print(get_routes(graph, N-1, M-1))