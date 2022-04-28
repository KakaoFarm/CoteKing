N, M = map(int, input().split())

graph = [[0]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = -1
    graph[b-1][a-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0 and graph[i][k] == graph[k][j]:
                graph[i][j] = graph [i][k]
                graph[j][i] = -graph[i][j]

answer = 0
for i in range(N):
    if graph[i].count(0) == 1:
        answer += 1

print(answer)
