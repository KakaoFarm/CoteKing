def solution(width, height, diagonals):
    
    MOD = 10000019
    dp = [[[0]*2 for _ in range(width+1)] for _ in range(height+1)]
    board = [[[0]*2 for _ in range(width+1)] for _ in range(height+1)]

    for x, y in diagonals:
        board[y-1][x][0] = 1
        board[y][x-1][1] = 1

    dp[0][0][0] = 1

    for x in range(height+1):
        for y in range(width+1):
            if x > 0:
                dp[x][y][0] = (dp[x][y][0] + dp[x-1][y][0]) % MOD
            if y > 0:
                dp[x][y][0] = (dp[x][y][0] + dp[x][y-1][0]) % MOD                

    for x in range(height+1):
        for y in range(width+1):
            if x > 0:
                dp[x][y][1] = (dp[x][y][1] + dp[x-1][y][1]) % MOD
            if y > 0:
                dp[x][y][1] = (dp[x][y][1] + dp[x][y-1][1]) % MOD
            if board[x][y][0]:
                dp[x][y][1] = (dp[x][y][1] + dp[x+1][y-1][0]) % MOD
            if board[x][y][1]:
                dp[x][y][1] = (dp[x][y][1] + dp[x-1][y+1][0]) % MOD

    answer = dp[-1][-1][1]
    return answer

'''
width * height의 격자가 있는데
대각선이 있는 경우도 있음. 대각선들의 위치는 diagonals에 담겨있음.
한쪽 끝에서 다른쪽 끝으로 가는 경로 중 대각선을 딱 한번 지나는 최단경로의 갯수 구하기
'''