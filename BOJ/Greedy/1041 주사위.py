import sys

N = int(sys.stdin.readline())
dice = list(map(int,sys.stdin.readline().strip().split()))
A = min(dice[0],dice[5])
B = min(dice[1],dice[4])
C = min(dice[2],dice[3])
nums = [A, B, C]
nums.sort()

if N == 1:
    ans = sum(dice)-max(dice)
else:
    ans = nums[0]*(5*((N-2)**2) + 12*(N-2) + 8) + nums[1]*(8*(N-2) + 8) + nums[2]*4

print(ans)
