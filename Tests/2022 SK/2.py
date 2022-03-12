def solution(n, clockwise):
    answer = [[0]*n for _ in range(n)]

    if clockwise:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
    else:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

    x = 0
    y = 0    
    i = 0
    cnt = 1
    while True:
        answer[x][y], answer[y][n-1-x], answer[n-1-x][n-1-y], answer[n-1-y][x] = cnt, cnt, cnt, cnt
        if answer[x + dx[i]][y + dy[i]] != 0:
            i = (i + 1) % 4
        x += dx[i]
        y += dy[i]
        if cnt >= (n * n / 4):
            break
        cnt += 1

    return answer

'''
n*n배열인데 네 귀퉁이부터 시작해서 시계방향 or 반시계방향으로 숫자 채워나가는 배열 만들기
1 2 3 1
3 4 4 2
2 4 4 3
1 3 2 1 
'''