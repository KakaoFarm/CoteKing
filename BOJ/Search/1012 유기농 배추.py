import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())

    graph = [[0]*M for _ in range(N)]
    for _ in range(K):
        Y, X = map(int, sys.stdin.readline().rstrip().split())
        graph[X][Y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    answer = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i, j))
                graph[i][j] = 2
                while queue:
                    X, Y = queue.popleft()
                    
                    for k in range(4):
                        NX = X + dx[k]
                        NY = Y + dy[k]
                        if not(0 <= NX < N and 0<= NY < M):
                            continue
                        if graph[NX][NY] == 1:
                            graph[NX][NY] = 2
                            queue.append((NX, NY))
                answer += 1


    print(answer)
