N, M = map(int, input().split())

def solution(i, length, answer):
    if length == M:
        answer = map(str, answer)
        print(" ".join(answer))
        return True
    for k in range(i+1, N+1):
        new_answer = answer + [k]
        solution(k, length+1, new_answer)

solution(0,0,[])
