def solution(money, costs):
    value = [1, 5, 10, 50, 100, 500]
    eff = [((value[i] / costs[i]), value[i], costs[i]) for i in range(6)]
    eff.sort(key = lambda x:x[0], reverse=True)

    answer = 0
    cur_money = money
    for i in range(6):
        Q = cur_money // eff[i][1]
        answer += eff[i][2] * Q
        cur_money -= eff[i][1] * Q

    return answer
'''
costs: 1, 5, 10, 50, 100, 500원 동전의 생산단가
money: 목표가격
answer: 최소비용
'''
