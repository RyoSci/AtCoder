n = int(input())

res = []
for i in range(1 << n):
    stack = []
    ans = ""
    for j in range(n):
        if i >> j & 1:
            if len(stack) == 0 or len(stack) != 0 and stack[-1] == ")":
                stack.append(")")
            else:
                stack.pop()
            ans += ")"
        else:
            stack.append("(")
            ans += "("
    if len(stack) == 0:
        res.append(ans)

res.sort()
for i in res:
    print(i)
