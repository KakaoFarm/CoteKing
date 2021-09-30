N, M = map(int, input().split())
nums = list(map(int, input().split()))

A = N // 2
part_A = {0:1}
part_B = {0:1}
for num in nums[:A]:
    temp = part_A.copy()
    for partial_sum in part_A:
        count = part_A[partial_sum]
        new_sum = partial_sum + num
        if new_sum in temp:
            temp[new_sum] += count
        else:
            temp[new_sum] = count
    part_A = temp.copy()

for num in nums[A:]:
    temp = part_B.copy()
    for partial_sum in part_B:
        count = part_B[partial_sum]
        new_sum = partial_sum + num
        if new_sum in temp:
            temp[new_sum] += count
        else:
            temp[new_sum] = count
    part_B = temp.copy()

answer = 0
for partial_sum in part_B:
    target = M - partial_sum
    if target in part_A:
        answer += part_A[target] * part_B[partial_sum]

if M == 0:
    answer -= 1
print(answer)
