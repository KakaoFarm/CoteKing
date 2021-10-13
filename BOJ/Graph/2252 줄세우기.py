from collections import deque

N, K = map(int, input().split())

parents = [1] + [0]*(N)
children = [[] for _ in range(N+1)]

for _ in range(K):
    a, b = map(int, input().split())
    parents[b] += 1
    children[a].append(b)

queue = deque()
for i in range(N+1):
    if parents[i] == 0:
        queue.append(i)
while queue:
    parent = queue.popleft()
    print(parent, end=" ")
    for child in children[parent]:
        parents[child] -= 1
        if parents[child] == 0:
            queue.append(child)
