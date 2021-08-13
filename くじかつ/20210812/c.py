n = int(input())
c = list(input())
c_c = []
tmp = c[0]

for i in range(1, n):
    if c[i] != c[i-1]:
        c_c.append(tmp)
        tmp = c[i]
    else:
        tmp += c[i]

if len(tmp) != 0:
    c_c.append(tmp)

if len(c_c) == 1:
    print(0)
elif len(c_c) == 2 and c_c[0][0] == "R":
    print(0)
else:
    r = 0
    w = 0
    for i in range(n):
        if c[i] == "R":
            r += 1
        else:
            w += 1
    t = "R"*r+"W"*w
    res = 0
    for i in range(n):
        if t[i] != c[i]:
            res += 1
    print(res//2)
