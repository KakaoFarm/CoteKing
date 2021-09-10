def solution(s):
    length = len(s)
    answer = length
    for divider in range(1, length//2+1):
        value = 0
        units = int(length // divider)
        temp = [] * divider
        count = 0
        for i in range(units):
            if temp == s[i*divider:(i+1)*divider]:
                count += 1
                if count == 1 or count == 9 or count == 99 or count == 999:
                    value += 1
            else:
                temp = s[i*divider:(i+1)*divider]
                count = 0
                value += divider
        value += length % divider
        answer = min(answer, value)
    return answer

print(solution("xxxxxxxxxxyyy"))
