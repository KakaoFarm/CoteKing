V, E = map(int, input().split())
edges = []
parent = []
for _ in range(E):
    X, Y, W = map(int, input().split())
    edges.append((X, Y, W))
edges.sort(key=lambda x:x[2])
for i in range(V+1):
    parent.append(i)

def get_group(X):
    if parent[X] == X:
        return X
    else:
        parent[X] = get_group(parent[X])
        return parent[X]

def in_same_group(X, Y):
    A = get_group(X)
    B = get_group(Y)
    if A == B:
        return True
    else:
        return False

def union(X, Y):
    A = get_group(X)
    B = get_group(Y)
    parent[B] = A

answer = 0
count = 0
for edge in edges:
    X, Y, W = edge
    if not in_same_group(X, Y):
        union(X, Y)
        answer += W
        count += 1
        if count == V-1:
            break
print(answer)
