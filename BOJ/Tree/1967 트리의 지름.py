import sys

sys.setrecursionlimit(10**4+1)

N = int(input())
children = dict()
child_dist = [[] for _ in range(N+1)]
for i in range(1, N+1):
    children[i] = []

for _ in range(N-1):
    P, C, W = map(int,input().split())
    children[P].append((C, W))

root = 1
if len(children[root]) == 1:
    children[children[root][0][0]].append((1, children[root][0][1]))
    root = children[root][0][0]
    children[1] = []
    

def get_max_distance(node):
    if not children[node]:
        return 0
    for edge in children[node]:
        child, weight = edge
        child_dist[node].append(get_max_distance(child) + weight)
    return max(child_dist[node])

get_max_distance(root)
answer = 0
for node in range(1, N+1):
    if len(child_dist[node]) >= 2:
        child_dist[node].sort(reverse=True)
        answer = max(answer, sum(child_dist[node][:2]))
if N == 2:
    answer = children[root][0][1]

print(answer)
