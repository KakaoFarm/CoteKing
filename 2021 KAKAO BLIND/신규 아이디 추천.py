import re

def solution(new_id):
    
    answer = new_id.lower()

    targets = "~!@#$%^&*()=+[{]}:?,<>/"
    for target in targets:
        answer = answer.replace(target, "")

    answer = re.sub('(([.])\\2{1,})', '.', answer)

    if answer and answer[0] == ".":
        answer = answer[1:]
    if answer and answer[-1] == ".":
        answer = answer[:-1]

    if not answer:
        answer = "a"

    if len(answer) >= 16:
        answer = answer[:15]

    if answer[-1] == ".":
        answer = answer[:-1]

    while len(answer) <= 2:
        answer += answer[-1]

    return answer

