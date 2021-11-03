def gravity(board):
    columns = []
    for i in range(6):
        columns.append([row[i] for row in board])
    for i in range(6):
        while True:
            try:
                columns[i].remove(0)
            except:
                break
        while len(columns[i]) < 6:
            columns[i].append(0)
    
    board = [[column[i] for column in columns] for i in range(6)]

    return board

def boom(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False]*6 for _ in range(6)]
    boomed = False
    for m in range(6):
        for n in range(6):
            if board[m][n] != 0:
                count = 0
                locations = []
                stack = []
                color = board[m][n]
                stack.append((m, n))
                while stack:
                    x, y = stack.pop()
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    locations.append((x, y))
                    count += 1
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < 6 and 0 <= ny < 6 and board[nx][ny] == color:
                            stack.append((nx, ny))
                if count >= 3:
                    for location in locations:
                        x, y = location
                        board[x][y] = 0
                    boomed = True
    
    return board, boomed


        

def solution(macaron):
    board = [[0]*6 for _ in range(6)]
    for move in macaron:
        column, color = move
        board[5][column-1] = color
        board = gravity(board)
        board, boomed = boom(board)
        while boomed:
            board = gravity(board)
            board, boomed = boom(board)

    answer = []
    for row in board[::-1]:
        answer.append("".join(map(str, row)))
    return answer

print(boom([[1, 1, 4, 4, 4, 1], [2, 2, 1, 3, 0, 0], [4, 3, 2, 0, 0, 0], [0, 0, 3, 0, 0, 0], [0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
print(solution([[1,1],[1,2],[1,4],[2,1],[2,2],[2,3],[3,4],[3,1],[3,2],[3,3],[3,4],[4,4],[4,3],[5,4],[6,1]]))