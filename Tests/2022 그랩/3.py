import re
def solution(replies, n, k):
    return [0 if re.compile(f'([A-F]{{{n},}})\\1{{{k-1},}}').search(reply) else 1 for reply in replies]
