def solution(n, computers):
    answer = 0
    is_counted = [False]*n

    def count_network(start):
        if not is_counted[start]:
            is_counted[start] = True
            for i in range(n):
                if computers[start][i]:
                    count_network(i)
            return True
        return False
    for i in range(len(computers)):
        if count_network(i):
            answer += 1

    return answer
