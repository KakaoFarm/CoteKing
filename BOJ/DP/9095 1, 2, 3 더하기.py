import sys

targets = []
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    targets.append(int(sys.stdin.readline().rstrip()))

Dp = [-1]*(max(targets)+1)
Dp[:2] = [1,1]

def solution(Dp, n):
    if Dp[n] != -1:
        return Dp[n]
    else:
        if n == 2:
            Dp[n] = 2
        else:
            Dp[n] = solution(Dp, n-1) +  solution(Dp, n-2) +  solution(Dp, n-3)
        return Dp[n]

for target in targets:
    print(solution(Dp, target))
