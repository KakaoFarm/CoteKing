import sys

def test(target, test_num):
    if target == "+":
        if test_num > 0:
            return True
        else:
            return False
    if target == "0":
        if test_num == 0:
            return True
        else:
            return False
    if target == "-":
        if test_num < 0:
            return True
        else:
            return False

def possible_range(array, depth, N):
    n = N - depth
    if array[int(-n * (n+1) / 2)] == "+":
        return range(1,11)
    if array[int(-n * (n+1) / 2)] == "0":
        return range(0,1)
    if array[int(-n * (n+1) / 2)] == "-":
        return range(-10,0)

    
N = int(sys.stdin.readline().rstrip())
array = list(sys.stdin.readline().rstrip())
answer = [0]*N

def guess(N, array, depth, answer):
    stack = list()
    stack.append((answer[:], depth))
    while stack:
        answer, depth = stack.pop()
        for i in possible_range(array, depth, N):
            answer[depth] = i
            target = depth
            is_passed = 1
            for k in range(depth):
                rangee = answer[k:depth+1]
                is_passed = 1
                if not test(array[target], sum(answer[k:depth+1])):
                    is_passed = 0
                    break
                target += N - k - 1
            if is_passed == 1:
                if depth == N - 1:
                    return answer
                stack.append((answer[:], depth+1))

print(" ".join(map(str,guess(N, array, 0, answer))))
