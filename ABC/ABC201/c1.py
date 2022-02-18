s = input()

o = []
x = []

for i in range(len(s)):
    if s[i] == "o":
        o.append(str(i))
    elif s[i] == "x":
        x.append(str(i))

res = 0
for i in range(10000):
    i = str(i)
    i = i.zfill(4)
    ans = True
    for j in o:
        if j not in i:
            ans = False
            break
    for j in i:
        if j in x:
            ans = False
            break
    if ans:
        res += 1

print(res)
