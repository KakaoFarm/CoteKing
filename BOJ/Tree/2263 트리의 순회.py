N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
in_order_index = [-1]*(N+1)
for index, node in enumerate(in_order):
    in_order_index[node] = index

stack = []
stack.append((0, N-1, 0, N-1))
while stack:
    in_order_start, in_order_end, post_order_start, post_order_end = stack.pop()
    root = post_order[post_order_end]
    print(root, end=" ")
    root_index = in_order_index[root]
    left = root_index - in_order_start
    right = in_order_end - root_index
    if right:
        stack.append((root_index+1, in_order_end, post_order_start+left, post_order_end-1))
    if left:
        stack.append((in_order_start, root_index-1, post_order_start, post_order_start+left-1))
