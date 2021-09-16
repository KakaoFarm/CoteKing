S = input()

def solution(string):
    if "(" not in string:
        return len(string)
    else:
        start = string.index("(")
        count = 1
        end = start
        while count != 0:
            if string[end+1] == "(":
                count += 1
            elif string[end+1] == ")":
                count -= 1
            end += 1
        A = string[:start-1]
        B = string[start+1:end]
        C = string[end+1:]
        return len(A) + (int(string[start-1]) * solution(B)) + solution(C)

print(solution(S))