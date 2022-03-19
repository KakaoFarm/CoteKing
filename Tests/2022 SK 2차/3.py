from itertools import combinations

def diff(A, B, maximum):
    N = len(A)
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i][j] and not B[i][j]:
                cnt += 1
                if cnt >= maximum:
                    return N
    return cnt

def getMatrix(a):
    N = len(a) + 1
    result = [[0]*N for _ in range(N)]
    for x, y in a:
        x, y = min(x, y)-1, max(x, y)-1
        result[x][y] = 1
    return result

def solution(a, b, m):
    A = getMatrix(a)
    B = getMatrix(b)
    N = len(a) + 1
    answer = diff(A, B, 12)

    combos = list(combinations(list(range(1, N+1)), 2))
    for k in range(1, m+1):
        cur_combos = combinations(combos, k)
        for combo in cur_combos:
            arr = list(range(1, N+1))
            for change in combo:
                x, y = change
                arr[x-1], arr[y-1] = arr[y-1], arr[x-1]
            new_b = [0 for _ in range(N-1)]
            for i in range(N-1):
                new_b[i] = [arr[b[i][0]-1], arr[b[i][1]-1]]
            
            answer = min(answer, diff(A, getMatrix(new_b), answer))
            
    return answer

print(solution([[3, 4], [7, 2], [5, 4], [2, 3], [6, 5], [1, 2]], [[2, 1], [3, 6], [1, 4], [1, 5], [7, 1], [3, 2]], 2))
