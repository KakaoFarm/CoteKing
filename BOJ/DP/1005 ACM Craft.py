from collections import deque
import heapq

T = int(input())
answers = []
for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    next_builds = [[] for _ in range(N+1)]
    required_builds = [set() for _ in range(N+1)]
    for i in range(K):
        X, Y = map(int, input().split())
        next_builds[X].append(Y)
        required_builds[Y].add(X)
    built = set()
    W = int(input())
    answer = float('INF')
    heap = []
    for i in range(1, N+1):
        if required_builds[i] == set():
            heapq.heappush(heap, ((times[i], i)))
    while heap:
        time, node = heapq.heappop(heap)
        built.add(node)
        if node == W:
            answer = min(answer, time)
            continue
        for next_build in next_builds[node]:
            if required_builds[next_build].issubset(built):
                
                new_time = time + times[next_build]
                if new_time < answer:
                    heapq.heappush(heap, (new_time, next_build))
    answers.append(answer)
for answer in answers:
    print(answer)
