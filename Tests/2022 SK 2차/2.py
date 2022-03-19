import heapq
from collections import deque

def solution(arr, processes):
    answer = []
    answer_heap = []

    working = []
    ready = []
    waiting = deque()
    now = 0
    time = 0
    is_writing = 0

    for process in processes:
        waiting.append(process.split())

    while working or ready or waiting:
        while waiting and  int(waiting[0][1]) == now:
            process = waiting.popleft()
            p = int(process[1])
            if process[0] == "read":
                p += 1000
            heapq.heappush(ready, (p, process))

        while working and int(working[0][0]) == now:
            end, process = heapq.heappop(working)
            if process[0] == "write":
                i, j, X = process[3:]
                i = int(i)
                j = int(j)
                for k in range(i, j+1):
                    arr[k] = X
                is_writing -= 1
            else:
                i, j = process[3:]
                i = int(i)
                j = int(j)
                heapq.heappush(answer_heap, (int(process[1]), "".join(arr[i:j+1])))
        
        while ready and not is_writing:
            if working and ready[0][1][0] == "write":
                break
            p, process = heapq.heappop(ready)
            if process[0] == "write":
                is_writing += 1
            end = int(now) + int(process[2])
            heapq.heappush(working, (end, process))
        
        if working:
            time += 1
        now += 1

    while answer_heap:
        result = heapq.heappop(answer_heap)[1]
        answer.append(result)

    answer.append(str(time))

    return answer

print(solution(["1","1","1","1","1","1","1"], ["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]))
