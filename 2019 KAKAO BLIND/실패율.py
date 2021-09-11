def solution(N, stages):
    players = [0]*(N+2)
    for stage in stages:
        players[stage] += 1
    played = len(stages)
    failed = 0
    fail_rate = dict()
    for i in range(1, N+1):
        failed = players[i]
        played -= players[i-1]
        if played == 0:
            fail_rate[i] = 0
        else: 
            fail_rate[i] = failed / played
    answer = sorted(fail_rate.items(), reverse=True, key=lambda x:x[1])
    answer = [answer[i][0] for i in range(len(answer))]
    return answer

