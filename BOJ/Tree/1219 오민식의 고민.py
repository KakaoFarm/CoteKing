N, start, end, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, cost = map(int,input().split())
    edges.append([a, b, -cost])
values = list(map(int, input().split()))
for i in range(M):
    destination = edges[i][1]
    edges[i][2] += values[destination]

income = [-float("INF") for _ in range(N)]
income[start] = values[start]
answer = 0

def is_connected(city):
    is_visited = [False]*N
    stack = [city]
    while stack:
        cur = stack.pop()
        if cur == end:
            return True
        is_visited[cur] = True
        for edge in edges:
            if edge[0] == cur and not is_visited[edge[1]]:
                stack.append(edge[1])
    return False            

for i in range(N+1):
    for j in range(M):
        cur_city, next_city, money = edges[j]
        if income[cur_city] != -float("INF") and income[cur_city] + money > income[next_city]:
            income[next_city] = income[cur_city] + money
            if i >= N-1 and is_connected(next_city):
                answer = "Gee"
                break

if income[end] == -float("INF"):
    answer = "gg"
elif answer != "Gee":
    answer = income[end]

print(answer)
