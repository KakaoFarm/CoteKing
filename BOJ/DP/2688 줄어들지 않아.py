import sys

T = int(sys.stdin.readline().rstrip())
cases = []
for _ in range(T):
    cases.append(int(sys.stdin.readline().rstrip()))

largest_case = max(cases)

dp = [[0]*10 for _ in range(largest_case + 1)]
for i in range(largest_case + 1):
    dp[i][0] = 1

for i in range(1, largest_case + 1):
    for j in range(1, 10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

for case in cases:
    print(sum(dp[case]))