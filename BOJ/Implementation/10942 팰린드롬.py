import sys

N = int(sys.stdin.readline().rstrip())
nums = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
answer = [[False]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    S = i
    E = i
    while S >= 1 and E <= N:
        if nums[S] == nums[E]:
            answer[S][E] = True
            S -= 1
            E += 1
        else:
            break
for i in range(1, N):
    S = i
    E = i+1
    while S >= 1 and E <= N:
        if nums[S] == nums[E]:
            answer[S][E] = True
            S -= 1
            E += 1
        else:
            break

M = int(sys.stdin.readline().rstrip())
for _ in range(M):
    S, E = map(int, sys.stdin.readline().rstrip().split())
    if answer[S][E] == True:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
