def solution(registered_list, new_id):
    if new_id not in registered_list:
        return new_id

    idx = 0  
    for char in new_id:
        if char.isalpha():
           idx += 1
    S = new_id[:idx]
    if not new_id[idx:]:
        N = 0
    else:
        N = int(new_id[idx:])

    compare_list = []
    for id in registered_list:
        if id[:idx] == S:
            if id[idx:]:
                compare_list.append(int(id[idx:]))
            else:
                compare_list.append(0)

    L = len(compare_list)
    compare_list.sort()
    new_N = N
    i = compare_list.index(new_N)
    while compare_list[i] == N:
        i += 1
        N += 1
        if i == L:
            break

    answer = S + str(N)
    return answer

print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))