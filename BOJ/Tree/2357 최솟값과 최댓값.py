import sys
input = sys.stdin.readline
INF = float('INF')

N, M = map(int, input().split())

nums = [0]
for _ in range(N):
    nums.append(int(input()))
tree = [(INF, 0)]*(N*4)

def init(start, end, index):
    if start == end:
        tree[index] = (nums[start], nums[start])
        return tree[index]
    mid = (start+end) // 2
    a = init(start, mid, index*2)
    b = init(mid+1, end, index*2+1)
    tree[index] = (min(a[0], b[0]), max(a[1], b[1])) 
    return tree[index]


def query(start, end, index, left, right):
    if left > end or right < start:
        return (INF, 0)
    if left <= start and right >= end:
        return tree[index]
    mid = (start+end) // 2
    a = query(start, mid, index*2, left, right)
    b = query(mid+1, end, index*2+1, left, right)
    return (min(a[0], b[0]), max(a[1], b[1]))
    
    
init(1, N, 1)
for _ in range(M):
    left, right = map(int, input().split())
    print(*query(1, N, 1, left, right))
