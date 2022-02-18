from collections import deque
n = int(input())
s = input()

d = deque()
for i in range(n):
    if len(d) == 0:
        d.append(s[i])
    else:
        if s[i] == ")" and d[-1] == "(":
            d.pop()
        else:
            d.append(s[i])

l = 0
r = 0
for j in d:
    if j == ")":
        l += 1
    else:
        r += 1

print("("*l+s+")"*r)
