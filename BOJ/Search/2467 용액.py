N = int(input())
nums = list(map(int, input().split()))

i = 0
j = len(nums) - 1
solution = float("INF")
answer = [None, None]

while i < j:
    temp = nums[i] + nums[j]
    if abs(temp) < solution:
        solution = abs(temp)
        answer = [nums[i], nums[j]]
    if temp > 0:
        j -= 1
    elif temp < 0:
        i += 1
    else:
        break

answer = list(map(str, answer))
answer = " ".join(answer)
print(answer)