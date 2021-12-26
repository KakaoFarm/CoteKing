def get_pi(P): #pi함수를 구하기
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
    i = 0 #S(문자열)의 탐색 인덱스
    j = 0 #P(패턴)의 탐색 인덱스
    pi = get_pi(P)
    answers = []
    while i < M:
        if S[i] == P[j]:
            if j == N-1:
                answers.append(i-N+2)
                j = pi[j]
                i += 1
                continue
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = pi[j-1]
    return answers

S = input()
P = input()
answers = check(S, P)

print(len(answers))
print(*answers)
