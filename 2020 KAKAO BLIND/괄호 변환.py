def is_valid(p):
    sum = 0
    for i in range(len(p)):
        if p[i] == "(":
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            return False
    if sum == 0:
        return True
    else:
        return False

def reverse(p):
    reverse = ["a"]*len(p)
    for i in range(len(p)):
        if p[i] == "(":
            reverse[i] = ")"
        else:
            reverse[i] = "("
    return "".join(reverse)

def solution(p):
    if p == "":
        return ""
    if is_valid(p):
        return p
    N = len(p)
    sum = 0
    divider = 0
    for i in range(N):
        if p[i] == "(":
            sum += 1
        else: sum -=1
        if sum == 0:
            divider = i+1
            break
    u = p[:divider]
    v = p[divider:]
    if is_valid(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + reverse(u[1:-1])

print(solution("()))((()"))