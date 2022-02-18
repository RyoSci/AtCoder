s = input()
t = input()
res = len(t)
for i in range(0, len(s) - len(t) + 1):
    si = s[i:i + len(s)]
    tmp = len(t)
    for i in range(len(t)):
        if si[i] == t[i]:
            tmp -= 1
    res = min(res, tmp)

print(res)
