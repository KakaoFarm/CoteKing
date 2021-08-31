import sys

def max_value(graph, x, y):
    values = []
    try:
        values.append(graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x][y+3])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+3][y])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x+1][y] + graph[x][y+1] + graph[x+1][y+1])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x-1][y+2])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x+1][y+2])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+2][y-1])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+2][y+1])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x][y+1])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x][y-1])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x-1][y])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x+1][y])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x][y+1] + graph[x-1][y+1] + graph[x-1][y+2])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x][y+1] + graph[x+1][y+1] + graph[x+1][y+2])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x+1][y] + graph[x+1][y-1] + graph[x+2][y-1])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x+1][y] + graph[x+1][y+1] + graph[x+2][y+1])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x-1][y+1])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x+1][y+1])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+1][y-1])
    except:
        pass
    try:
        values.append(graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+1][y+1])
    except:
        pass
    if values:
        max_value = max(values)
    else:
        max_value = 0
    return max_value


N, M = map(int, sys.stdin.readline().rstrip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))

max_values = []
for i in range(N):
    for j in range(M):
        max_values.append(max_value(graph,i,j))

answer = max(max_values)
print(answer)