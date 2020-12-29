x = input()
stack = []
ans = 0
for i in x:
    if i == "T":
        if len(stack) != 0 and stack[-1] == "S":
            ans += 1
            stack.pop()
            continue
    stack.append(i)
print(len(x) - 2 * ans)
