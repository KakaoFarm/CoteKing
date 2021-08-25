from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque( [(0, 0)] )
    while queue:
        (sum, length) = queue.popleft()
        if length == len(numbers):
            if sum == target:
                answer += 1
        elif length < len(numbers):
            queue.append((sum+numbers[length], length+1))
            queue.append((sum-numbers[length], length+1))
    return answer   

print(solution([1, 1, 1, 1, 1],3))
