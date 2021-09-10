N = int(input())
key = list(input().split())

def is_validated(sign, previous_num, next_num):
    if sign == ">":
        if previous_num > next_num:
            return True
        else:
            return False
    elif sign == "<":
        if previous_num < next_num:
            return True
        else:
            return False

answers =[]

def Max_answer(key, depth, answer):
    if depth == len(key)+1:
        answers.append(answer)
        return True
    for i in range(9,-1,-1):
        if depth == 0:
            Max_answer(key, 1, answer + [i])
        else:
            if i not in answer and is_validated(key[depth-1], answer[depth-1], i):
                Max_answer(key, depth+1, answer + [i])

Max_answer(key, 0, [])
print("".join(map(str,answers[0])))
print("".join(map(str,answers.pop())))