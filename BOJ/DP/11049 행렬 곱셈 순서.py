N = int(input())
nums = []
a, b= map(int, input().split())
nums += [a, b]
for _ in range(N-1):
    a, b = map(int, input().split())
    nums.append(b)

dp = [[float('INF')]*(N+1) for _ in range(N+1)]

def solution(start, end):
    if dp[start][end] != float('INF'):
        return dp[start][end]
    if end - start == 1:
        return 0
    for i in range(start+1, end):
        dp[start][end] = min(dp[start][end], solution(start, i) + solution(i, end) + nums[start]*nums[i]*nums[end])
    value = dp[start][end]
    return value

print(solution(0, N))
