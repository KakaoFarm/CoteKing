from itertools import combinations

def solution(orders, course):
    answer = []
    for i in range(len(orders)):
        orders[i] = "".join(sorted(list(orders[i])))
    for N in course:
        max_value = 0
        temp_answer = []
        counter = dict()
        for order in orders:
            for combo in combinations(order, N):
                if combo in counter.keys():
                    counter[combo] += 1
                else:
                    counter[combo] = 1
        for combo in counter:
            if counter[combo] > max_value and counter[combo] > 1:
                max_value = counter[combo]
                temp_answer = ["".join(combo)]
            elif counter[combo] == max_value and counter[combo] > 1:
                temp_answer.append("".join(combo))
        answer += temp_answer
    answer.sort()
    return answer
