from collections import deque

n = int(input())
s = input()

stack = deque([])

res = 0
for i in range(n):
    if s[i] == "f":
        stack.append("f")
    elif s[i] == "o":
        if len(stack) != 0:
            if stack.pop() == "f":
                stack.append("fo")
            else:
                stack = deque([])
    elif s[i] == "x":
        if len(stack) != 0:
            if stack.pop() == "fo":
                res += 1
            else:
                stack = deque([])
    else:
        stack = deque([])

print(n - 3 * res)
