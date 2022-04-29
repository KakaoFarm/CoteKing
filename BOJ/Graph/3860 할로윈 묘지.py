answers = []
while True:
    W, H = map(int, input().split())
    if W == 0: break
    N = W * H
    G = int(input())
    INF = float("INF")
    times = [[INF]*H for _ in range(W)]
    times[0][0] = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    edges = []
    board = [[0]*H for _ in range(W)]

    for _ in range(G):
        x, y = map(int, input().split())
        board[x][y] = 1

    E = int(input())    
    for _ in range(E):
        x, y, nx, ny, t = map(int, input().split())
        board[x][y] = 2
        edges.append((x, y, nx, ny, t))

    for x in range(W):
        for y in range(H):
            if board[x][y] == 0 and not (x == W-1 and y == H-1):
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < W and 0 <= ny < H and board[nx][ny] != 1:
                        edges.append((x, y, nx, ny, 1))
    answer = 0
    for k in range(N):
        for edge in edges:
            x, y, nx, ny, t = edge
            if times[x][y] + t < times[nx][ny]:
                if k == N-1:
                    answer = "Never"
                    break
                times[nx][ny] = times[x][y] + t

    if answer != "Never":
        if times[W-1][H-1] == INF:
            answer = "Impossible"
        else:
            answer = times[W-1][H-1]
    answers.append(answer)

for answer in answers:
    print(answer)
