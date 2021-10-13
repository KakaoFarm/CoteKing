import sys

S = 0
M = int(sys.stdin.readline().rstrip())

def add(S, x):
    S |= 1<<x
    return S

def remove(S, x):
    S &= ~(1<<x)
    return S

def check(S, x):
    if S & (1<<x) > 0:
        return "1"
    else:
        return "0"

def toggle(S, x):
    S ^= 1<<x
    return S

def all():
    return 2**21-2

def empty():
    return 0

for _ in range(M):
    calculation = sys.stdin.readline().rstrip()
    if calculation == "all":
        S = all()
    elif calculation == "empty":
        S = empty()
    else:
        action, value = calculation.split()
        value = int(value)
        if action == "add":
            S = add(S, value)
        elif action == "check":
            sys.stdout.write(check(S, value) + "\n")
        elif action == "remove":
            S = remove(S, value)
        elif action == "toggle":
            S = toggle(S, value)
