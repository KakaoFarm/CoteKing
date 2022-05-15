def cal(i, cnt, n, k):
    if cnt == k-1:
        return costs[i]
    
    if i >= len(costs)-2:
        return 10**5
    
    result = 10**5
    for j in range(i+2, len(costs)-1):
        result = min(result, cal(j, cnt+1, n, k))
    if result == 10**5:
        return 10**5
    return result + costs[i]


def solution(bricks, n, k):
    global costs
    costs = [n - b for b in bricks]
    answer = 10**5
    for i in range(1, len(costs)-1):
        answer = min(answer, cal(i, 1, n, k))
    return answer

costs = []