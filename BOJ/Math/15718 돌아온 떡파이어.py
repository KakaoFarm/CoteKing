import math

def convert(X, MOD):
    result = []
    while X > 0:
        X, r = X // MOD, X % MOD
        result.append(r)
    return result


def C(n, r, MOD):
    result = 1
    length = len(n)
    for i in range(length):
        if (i < len(r)):
            k = r[i]
        else:
            k = 0
        if (n[i] < k):
            result = 0
        else:
            result *= (math.factorial(n[i]) // math.factorial(k) // math.factorial(n[i] - k))
    return result % MOD

def euclid(A, B):
    r1 = A
    r2 = B
    t1 = 1
    t2 = 0
    while r2 > 0:
        q = r1 // r2
        r1, r2 = r2, r1 - (r2 * q)
        t1, t2 = t2, t1 - (t2 * q)
    return t1

def solution(a, b):
    A = 97
    B = 1031
    # A * x + B * y = 1
    x = euclid(A, B)
    y = (1 - (A * x)) // B
    answer = ((a * B * y) + (b * A * x)) % 100007
    return answer


T = int(input())
for _ in range(T):

    N, M = map(int, input().split())
    if N == 0 and M == 1:
        print(1)
    elif N < M-1 or M == 1:
        print(0)
    else:
        n1 = convert(N-1, 97)
        r1 = convert(N-M+1, 97)
        answer1 = C(n1, r1, 97)
        n2 = convert(N-1, 1031)
        r2 = convert(N-M+1, 1031)
        answer2 = C(n2, r2, 1031)
        answer = solution(answer1, answer2)
        print(answer)
