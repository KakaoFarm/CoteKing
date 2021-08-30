from collections import deque
import sys

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(input()))

queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_longest_distance(start_x, start_y):
    is_visited = [[0]*M for _ in range(N)]
    max_length = 0
    is_visited[start_x][start_y] = 1        
    queue.append((start_x,start_y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == "L" and is_visited[nx][ny] == 0:
                is_visited[nx][ny] = is_visited[x][y] + 1
                max_length = max(max_length, is_visited[nx][ny])
                queue.append((nx, ny))
    return max_length - 1

answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == "L":
            answer = max(get_longest_distance(i,j), answer)

print(answer)
