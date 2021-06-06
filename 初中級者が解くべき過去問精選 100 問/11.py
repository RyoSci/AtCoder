n, m = map(int, input().split())
switches_of_bulbs = []

for i in range(m):
    _, *s = map(int, input().split())
    switches_of_bulbs.append(s)

p = list(map(int, input().split()))

res = 0
for i in range(1 << n):
    on_off = [0]*n
    for j in range(n):
        if i >> j & 1:
            on_off[j] = 1
    for j in range(m):
        s = switches_of_bulbs[j]
        sum_bulbs = 0
        for k in s:
            sum_bulbs += on_off[k-1]
        if sum_bulbs % 2 != p[j]:
            break
    else:
        res += 1

print(res)
