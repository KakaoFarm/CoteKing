N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def solution(nums, answer):
    if len(nums) == N - M:
        answer = list(map(str, answer))
        print(" ".join(answer))
    for num in nums:
        new_nums = nums[:]
        new_nums.remove(num)
        new_answer = answer + [num]
        solution(new_nums, new_answer)

solution(nums, [])