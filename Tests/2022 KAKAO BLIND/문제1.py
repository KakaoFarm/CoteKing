def solution(id_list, report, k):
    answer = [0]*len(id_list)
    user_number = dict()
    reported = dict()
    for i in range(len(id_list)):
        user_number[id_list[i]] = i
        reported[id_list[i]] = set()
    for log in report:
        reporter, bad_guy = log.split()
        reported[bad_guy].add(reporter)
    for id in id_list:
        if len(reported[id]) >= k:
            for reporter in reported[id]:
                answer[user_number[reporter]] += 1
    return answer
