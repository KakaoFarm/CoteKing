infix = input()
stack = []

for char in infix:
    if char.isalpha():
        print(char, end="")
    else:
        if char == ")":
            while stack[-1] != "(":
                print(stack.pop(), end="")
            stack.pop()
        else:
            if char in ("*", "/"):
                while stack and stack[-1] in ("*", "/"):
                    print(stack.pop(), end="")
            elif char in ("+", "-"):
                while stack and stack[-1] in ("+", "-", "*", "/"):
                    print(stack.pop(), end="")
            stack.append(char)
while stack:
    print(stack.pop(), end="")
