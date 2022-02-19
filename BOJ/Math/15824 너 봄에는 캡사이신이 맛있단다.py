import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
MOD = 1000000007

pow2 = [1]*N
for i in range(1, N):
    pow2[i] = (pow2[i-1] * 2) % MOD

answer = 0
for i in range(N):
    answer += arr[i]*(pow2[i] - pow2[N-1-i])

print(answer % MOD)
