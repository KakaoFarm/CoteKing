def solution(record):
    nicknames = dict()
    answer = []
    for log in record:
        cur_log = log.split()
        if cur_log[0] == "Enter" or cur_log[0] == "Change":
            nicknames[cur_log[1]] = cur_log[2]
    for log in record:
        cur_log = log.split()
        nickname = nicknames[cur_log[1]]
        if cur_log[0] == "Enter":
            message = f"{nickname}님이 들어왔습니다."
            answer.append(message)
        elif cur_log[0] == "Leave":
            message = f"{nickname}님이 나갔습니다."
            answer.append(message)
    
    return answer

