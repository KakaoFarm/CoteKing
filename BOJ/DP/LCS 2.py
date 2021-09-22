A = input()
B = input()
M = len(A)
N = len(B)

dp = [[[0,""] for _ in range(M+1)] for _ in range(N+1)]

for b in range(1,N+1):
    for a in range(1,M+1):
        if B[b-1] == A[a-1]:
            dp[b][a][0] = dp[b-1][a-1][0] + 1
            dp[b][a][1] = dp[b-1][a-1][1] + B[b-1]
        else:
            if dp[b-1][a][0] >= dp[b][a-1][0]:
                dp[b][a][0] = dp[b-1][a][0]
                dp[b][a][1] = dp[b-1][a][1]
            else:
                dp[b][a][0] = dp[b][a-1][0]
                dp[b][a][1] = dp[b][a-1][1]

print(dp[N][M][0])
print(dp[N][M][1])
