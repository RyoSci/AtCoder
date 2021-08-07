n = int(input())
s = input()
a = []
pre = s[0]
cnt = 0
for i in range(n):
    if s[i] == pre:
        cnt += 1
    else:
        a.append([pre, cnt])
        pre = s[i]
        cnt = 1

a.append([pre, cnt])

res = 0
b = 0
w = 0
for i in range(len(a)-1):
    if a[i][0] == "#":
        b += a[i][1]
        w += a[i+1][1]
        if b <= w:
            res += b
            b = 0
            w = 0
res += w

print(res)
