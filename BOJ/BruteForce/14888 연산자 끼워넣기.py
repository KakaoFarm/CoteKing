N = int(input())
nums = list(map(int, input().split()))
counts = list(map(int, input().split()))
signs = []

signs += ["+"]*counts[0]
signs += ["-"]*counts[1]
signs += ["*"]*counts[2]
signs += ["/"]*counts[3]

def solution(counts, result):
    N = sum(counts)
    if N == 0:
        return [result]
    results = []
    if counts[0] > 0:
        new_counts = counts[:]
        new_counts[0] -= 1
        new_result = result + nums[-N]
        results += solution(new_counts, new_result)
    if counts[1] > 0:
        new_counts = counts[:]
        new_counts[1] -= 1
        new_result = result - nums[-N]
        results += solution(new_counts, new_result)
    if counts[2] > 0:
        new_counts = counts[:]
        new_counts[2] -= 1
        new_result = result * nums[-N]
        results += solution(new_counts, new_result)
    if counts[3] > 0:
        new_counts = counts[:]
        new_counts[3] -= 1
        if result < 0 and nums[-N] > 0:
            new_result = -((-result) // nums[-N])
        else:
            new_result = result // nums[-N]
        results += solution(new_counts, new_result)
    return results

print(max(solution(counts, nums[0])))
print(min(solution(counts, nums[0])))