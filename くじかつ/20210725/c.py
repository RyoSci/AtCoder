from collections import deque
s = input()

d = deque()
flip = 0

for i in s:
    if i == "R":
        flip ^= 1
    else:
        if flip:
            d.appendleft(i)
        else:
            d.append(i)

s = []
for i in d:
    if len(s) == 0:
        s.append(i)
    else:
        if s[-1] == i:
            s.pop()
        else:
            s.append(i)
if flip:
    s = s[::-1]

print(*s, sep="")
