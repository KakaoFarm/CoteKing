def check(key, lock, down, right, rotate):
    M = len(key)
    N = len(lock)
    test_lock = [lock[i][:] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if 0 <= M+i-down-1 < M and 0 <= M+j-right-1 < M:
                test_lock[i][j] += key[M+i-down-1][M+j-right-1]
    for i in range(N):
        for j in range(N):
            if test_lock[i][j] != 1:
                return False
    return True

def key_rotated(key, n):
    M = len(key)
    new_key = [[0]*M for _ in range(M)]
    if n == 0:
        return key
    if n == 1:
        for i in range(M):
            for j in range(M):
                new_key[j][M-1-i] = key[i][j]
        return new_key
    if n == 2:
        for i in range(M):
            for j in range(M):
                new_key[M-1-i][M-1-j] = key[i][j]
        return new_key
    if n == 3:
        for i in range(M):
            for j in range(M):
                new_key[M-1-j][i] = key[i][j]
        return new_key


def solution(key, lock):
    M = len(key)
    N = len(lock)
    for rotate in range(4):
        for x in range(N+M-1):
            for y in range(N+M-1):
                if check(key_rotated(key, rotate), lock, x, y, rotate):
                    return True
    return False


