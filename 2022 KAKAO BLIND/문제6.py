def solution(board, skill):
    answer = 0
    for action in skill:
        s_type, r1, c1, r2, c2, degree = action
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                if s_type == 1:
                    board[x][y] -= degree
                if s_type == 2:
                    board[x][y] += degree
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] > 0:
                answer += 1
    return answer

# 효율성 검사 실패(바라지도 않았지만..)
