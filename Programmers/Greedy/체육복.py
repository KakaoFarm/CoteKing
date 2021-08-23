def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    no_clothes = lost[:]
    for bad in lost:
        if bad in reserve:
            no_clothes.remove(bad)
            reserve.remove(bad)
            continue
        if bad - 1 in reserve:
            no_clothes.remove(bad)
            reserve.remove(bad - 1)
            continue
        if bad + 1 in reserve and bad + 1 not in lost:
            no_clothes.remove(bad)
            reserve.remove(bad + 1)
    answer = n - len(no_clothes)
    return answer

print(solution(5,[4,2],[3,5]))