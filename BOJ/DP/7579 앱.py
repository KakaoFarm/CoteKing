N, M = map(int, input().split())
values = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
dp = [[0]*(N+1) for _ in range(10001)]
answer = 0

for i in range(10001): #사용 코스트
    for j in range(1, N+1):
        if costs[j] <= i:
            dp[i][j] = max(dp[i][j-1], dp[i-costs[j]][j-1]+values[j])
        else:
            dp[i][j] = dp[i][j-1]
    if max(dp[i]) >= M:
        answer = i
        break

print(answer)
