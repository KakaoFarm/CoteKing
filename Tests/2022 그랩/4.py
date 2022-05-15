def parse(x):
    n = int(x**(1/2))
    return n, x - (n**2)

def isValid(x, y):
    global N
    if 0 <= x < N and y <= (x * 2):
        return True
    return False

def check(k, cnt, rooks):
    global N
    global board

    
    x, y = parse(k)
    if cnt == rooks:
        return 1

    deleted = []

    a, b = x, y
    if b % 2 == 1:
        b -= 1
    else:
        a += 1
        b += 1
    while isValid(a, b):
        if board[a][b] == 0:
            deleted.append((a, b))
        board[a][b] = cnt
        if b % 2 == 1:
            b -= 1
        else:
            a += 1
            b += 1

    a, b = x, y+1
    while isValid(a, b):
        if board[a][b] == 0:
            deleted.append((a, b))
        board[a][b] = cnt
        b += 1

    a, b = x, y+1
    if b % 2 == 1:
        a += 1
    while isValid(a, b):
        if board[a][b] == 0:
            deleted.append((a, b))
        board[a][b] = cnt
        b += 1
        if b % 2 == 1:
            a += 1

    result = 0
    for p in range(k+1, N**2):
        x, y = parse(p)
        if board[x][y] == 0:
            result += check(p, cnt+1, rooks)
    
    for x, y in deleted:
        board[x][y] = 0

    return result
        


def solution(n, rooks):
    answer = 0
    global N
    global board

    N = n
    board = [[0]*(2*i+1) for i in range(n)]

    for i in range(n**2):
        a, b = parse(i)
        board[a][b] = 1
        answer += check(i, 1, rooks)
    
    return answer

N = 0
board = []
