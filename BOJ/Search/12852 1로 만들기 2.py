from collections import deque

N = int(input())

answer = []
queue = deque()
queue.append((0, [N]))

while queue:
    depth, answer = queue.popleft()
    if answer[-1] == 1:
        print(depth)
        answer = list(map(str, answer))
        print(" ".join(answer))
        break
    if answer[-1] % 3 == 0:
        new_answer = answer + [int(answer[-1] / 3)]
        queue.append((depth+1, new_answer))
    if answer[-1] % 2 == 0:
        new_answer = answer + [int(answer[-1] / 2)]
        queue.append((depth+1, new_answer))
    new_answer = answer + [answer[-1] - 1]
    queue.append((depth+1, new_answer))
