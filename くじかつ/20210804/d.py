n, x, m = map(int, input().split())

d = dict()
a = x
num = [0]*10**6
tmp = a
for i in range(10**6):
    if a in d:
        cycle = i-d[a]
        start = d[a]
        cycle_num = tmp - num[d[a]]
        break
    else:
        d[a] = i
        num[i] = tmp
    a = (a*a) % m
    tmp += a

res = 0
if n > start+cycle:
    res += (n-start) // cycle*cycle_num
    n = start+(n-start) % cycle

a = x
for i in range(n):
    res += a
    a = a*a % m
print(res)
