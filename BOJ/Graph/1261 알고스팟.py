import heapq

M, N = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input())))
minimum = [[10**5]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
heap = []
heapq.heappush(heap, (0, 0, 0))
while heap:
    cnt, x, y = heapq.heappop(heap)
    if (x == N-1 and y == M-1):
        print(cnt)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N and 0 <= ny < M):
            newCnt =  cnt +board[nx][ny]
            if (newCnt < minimum[nx][ny]):
                minimum[nx][ny] = newCnt
                heapq.heappush(heap, (newCnt, nx, ny))
