N, K = map(int, input().split())

prev_set = {N}
new_set = {N}
is_visited = [False]*100002

if N <= K:
    i = 0   
    while True:
        temp_set = set()
        for j in new_set:
            while 0 < j <= 50000:
                j *= 2
                if not is_visited[j]:
                    temp_set.add(j)
                    is_visited[j] = True
        new_set |= temp_set
        
        if K in new_set:
            break

        i += 1
        prev_set = new_set
        new_set = set()

        for j in prev_set:
            if j > 1 and not is_visited[j-1]:
                new_set.add(j-1)
                is_visited[j-1] = True
            if j < 100000 and not is_visited[j+1]:
                new_set.add(j+1)
                is_visited[j+1] = True
else:
    i = N - K

print(i)
