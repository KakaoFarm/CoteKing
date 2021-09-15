K = int(input())

def solution(start, goal, N):
    if N == 1:
        print(f"{start} {goal}")
        return 
    temp = 6 - start - goal
    solution(start, temp, N-1)
    print(f"{start} {goal}")
    solution(temp, goal, N-1)       

print(2**K - 1)
solution(1, 3, K)
