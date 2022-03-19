def solution(n, m, k, records):
    answer = []

    distinct = len(set(records[0]))
    
    dists = [n]*(distinct+1)

    for record in records:
        record = sorted(list(set(record)))
        dists[0] = min(dists[0], record[0])
        dists[-1] = min(dists[-1], n + 1 - record[-1])
        for i in range(1, distinct):
            dists[i] = min(dists[i], record[i] - record[i-1])
    
    nums = [0]
    for i in range(distinct):
        nums.append(min(nums[-1] + dists[i], m + i - distinct + 1))
    del nums[0]
    
    password = records[0]
    used_nums = sorted(list(set(password)))
    dic = dict()
    for i in range(distinct):
        dic[used_nums[i]] = nums[i]

    for i in range(k):
        answer.append(dic[password[i]])

    return answer

print(solution(8, 4, 4, [[1, 5, 1, 3], [5, 7, 5, 6]]))