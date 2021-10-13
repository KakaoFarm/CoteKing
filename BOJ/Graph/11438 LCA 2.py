import sys 

LOG = 18 #2**17 > 100000
N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
parent = [[0]*LOG for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[A].append(B)
    graph[B].append(A)
depth = [-1]*(N+1)

parent[1][0] = -1
stack = [(1, 0)]
while stack:
    node, node_depth = stack.pop()
    depth[node] = node_depth
    for child in graph[node]:
        if parent[child][0] == 0:
            parent[child][0] = node
            stack.append((child, node_depth+1))
parent[1][0] = 0


for i in range(1, LOG):
    for node in range(1, N+1):
        parent[node][i] = parent[parent[node][i-1]][i-1]

M = int(sys.stdin.readline().rstrip())
for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    if depth[A] > depth[B]:
        A, B = B, A

    i = LOG - 1
    for i in range(LOG-1, -1, -1):
        if depth[A] <= depth[parent[B][i]]:
            B = parent[B][i]
            i -= 1

    if A == B:
        sys.stdout.write(str(A) + "\n")
        continue

    for i in range(LOG-1, -1, -1):
        if parent[A][i] != parent[B][i]:
            A = parent[A][i]
            B = parent[B][i]
    
    sys.stdout.write(str(parent[A][0]) + "\n")
