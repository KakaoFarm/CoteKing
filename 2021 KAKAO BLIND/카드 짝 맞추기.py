from collections import deque

def count_inputs(board, start, end):
    is_visited = [[0]*4 for _ in range(4)]
    is_visited[start[0]][start[1]] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((start, 0))
    while queue:
        cur, count = queue.popleft()
        if cur[0] == end[0] and cur [1] == end[1]:
            return count
        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if is_visited[nx][ny] == 0:
                    is_visited[nx][ny] = 1
                    queue.append(((nx, ny), count+1))
                if board[nx][ny] == 0:
                    nnx = cur[0] + 2*dx[i]
                    nny = cur[1] + 2*dy[i]
                    if 0 <= nnx < 4 and 0 <= nny < 4:
                        if (i <= 1 and (nnx == 0 or nnx == 3)) or (i >= 2 and (nny == 0 or nny == 3)) or board[nnx][nny] != 0:
                            if is_visited[nnx][nny] == 0:
                                is_visited[nnx][nny] = 1
                                queue.append(((nnx, nny), count+1))
                        else:
                            nnnx = cur[0] + 3*dx[i]
                            nnny = cur[1] + 3*dy[i]
                            if is_visited[nnx][nny] == 0:
                                is_visited[nnnx][nnny] = 1
                                queue.append(((nnnx, nnny), count+1))

def delete_pair(board, locations, cards, start, inputs):
    if len(cards) == 0:
        return [inputs]
    results = []
    for card in cards:
        for i in range(2):
            moves = count_inputs(board, start, locations[card][i])
            moves += count_inputs(board, locations[card][i], locations[card][1-i])
            new_board = [board[i][:] for i in range(len(board))]
            new_board[locations[card][0][0]][locations[card][0][1]] = 0
            new_board[locations[card][1][0]][locations[card][1][1]] = 0
            new_cards = cards[:]
            new_cards.remove(card)
            results += delete_pair(new_board, locations, new_cards, locations[card][1-i], inputs+moves)
    return results
            

def solution(board, r, c):
    locations = [[] for _ in range(7)]
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                locations[board[i][j]].append((i,j))
    for i in range(6, -1, -1):
        if not locations[i]:
            del locations[i]
    cards = list(range(len(locations)))
    results = delete_pair(board, locations, cards, (r,c), 0)
    answer = min(results) + 2*len(locations)
    return answer

print(solution([[3,0,4,2],[4,0,1,0],[5,1,0,6],[2,6,5,3]], 0, 0))