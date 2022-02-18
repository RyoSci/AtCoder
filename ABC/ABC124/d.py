n, k = map(int, input().split())
s = input()

t = []
pre = s[0]
tmp = 0
for i in range(n):
    if s[i] == pre:
        tmp += 1
    else:
        t.append(tmp)
        tmp = 1
        pre = s[i]
t.append(tmp)

tmp = 0
if s[0] == "0":
    r = 2 * k
else:
    r = 2 * k + 1
l = 0
tmp = sum(t[l:min(r, len(t))])

res = tmp
flag = False
r -= 1
if s[0] == "0":
    tmp -= t[0]
    l = 1
else:
    tmp -= sum(t[0:2])
    l = 2

while 1:
    for i in range(2):
        if r + 1 < len(t):
            r += 1
            tmp += t[r]
            res = max(res, tmp)
        else:
            flag = True
            break
    if flag:
        break
    tmp -= sum(t[l:l + 2])
    l += 2

print(res)
