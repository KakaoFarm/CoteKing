def get_pi(P): 
    N = len(P)
    pi = [0]*N
    i = 0
    j = 1
    while j < N:
        if P[i] == P[j]: 
            pi[j] = i+1
            i += 1
            j += 1
        else:
            if i == 0:
                j += 1
            else:
                i = pi[i-1]
    return pi

def check(S, P):
    N = len(P)
    M = len(S)
    i = 0 
    j = 0 
    pi = get_pi(P)
    while i < M:
        if S[i] == P[j]:
            if j == N-1:
                return True
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = pi[j-1]
    return False

def solution(goods):
    answers = []

    for good in goods:
        N = len(good)
        keys = []
        for k in range(1, N+1):
            for i in range(N-k+1):
                P = good[i:i+k]
                for other in goods:
                    if other != good and check(other, P):
                        break
                else:
                    if P not in keys:
                        keys.append(P)
            if keys:
                break
        if keys:
            answers.append(" ".join(sorted(keys)))
        else:
            answers.append("None")

    return answers

print(solution(["abcdeabcd","cdabe","abce","bcdeab"]))
