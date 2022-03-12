from collections import deque

def solution(n, edges):
    children = [[] for _ in range(n)]
    paths = [[] for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    for edge in edges:
        i, j = edge[0], edge[1]
        paths[i].append(j)
        paths[j].append(i)
    
    queue = deque()
    for x in range(n):
        if len(paths[x]) == 1:
            queue.append(x)
    
    while queue:
        x = queue.popleft()
        for node in paths[x]:
            if not visit[node][x]:
                x_sum = sum(children[x])
                children[x].append(sum(children[node]) + 1)
                children[node].append(x_sum + 1)
                visit[x][node] = True
                queue.append(node)
    
    answer = 0
    for x in range(n):
        answer += count_answer(children[x])    

    return answer

def count_answer(children):
    children_sum = sum(children)
    result = 0
    n = len(children)
    for i in range(n):
        result += children[i] * (children_sum - children[i])
    result = result
    return result

'''
트리에서
i부터 j까지 거리 + j부터 k까지 거리 == i부터 k까지 거리 <-를 만족하는 (i,j,k) 순서쌍 갯수 구하기
'''