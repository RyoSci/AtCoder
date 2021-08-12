n, c, k = map(int, input().split())
t = sorted([int(input()) for _ in range(n)])

res = 0
bus = []

for i in range(n):
    if len(bus) == 0:
        bus.append(t[i])
    elif len(bus) == c:
        res += 1
        bus = [t[i]]
    else:
        if bus[0]+k >= t[i]:
            bus.append(t[i])
        else:
            res += 1
            bus = [t[i]]

if len(bus) != 0:
    res += 1

print(res)
