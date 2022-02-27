import sys
input = sys.stdin.readline

def euclid(A, B):
    r1 = A
    r2 = B
    t1 = 1
    t2 = 0
    while r2 > 0:
        q = r1 // r2
        r1, r2 = r2, r1 - (r2 * q)
        t1, t2 = t2, t1 - (t2 * q)
    return r1, t1

def solution(A, B, a, b):
    G = euclid(A, B)[0]
    L = A * B // G
    if a % G != b % G:
        return False
    A //= G
    B //= G
    # A * x + B * y = 1
    x = euclid(A, B)[1]
    y = (1 - (A * x)) // B
    answer = ((a * B * y) + (b * A * x)) % L
    return L, answer

T = int(input())
for _ in range(T):
    A, B, C, a, b, c = map(int, input().split())
    temp = solution(A, B, a, b)
    if temp:
        D, d = temp
        temp = solution(C, D, c, d)
        if temp:
            print(temp[1])
        else:
            print(-1)
    else:
        print(-1)
