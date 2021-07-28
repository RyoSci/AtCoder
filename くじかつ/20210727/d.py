k, t = map(int, input().split())
a = list(map(int, input().split()))
b = []
for i in range(t):
    b.append([a[i], i])

b.sort(reverse=True)
res = 0
pre = -1

for i in range(k):
    if b[0][1] == pre:
        if len(b) > 1 and b[1][0] != 0:
            b[1][0] -= 1
            pre = b[1][1]
        else:
            res += 1
            b[0][0] -= 1
    else:
        b[0][0] -= 1
        pre = b[0][1]
    b.sort(reverse=True)

print(res)
