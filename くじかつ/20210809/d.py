n, m = map(int, input().split())

ks = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

res = 0
for i in range(1 << n):
    sw = [0]*n
    for j in range(n):
        if i >> j & 1:
            sw[j] = 1
    light = [0]*m
    for j in range(m):
        k, *s = ks[j]
        for si in s:
            light[j] += sw[si-1]
            light[j] %= 2
    if light == p:
        res += 1

print(res)
