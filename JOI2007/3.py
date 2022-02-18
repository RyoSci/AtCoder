n = int(input())
pillar_pos = []
pillar_set = set()
for i in range(n):
    x, y = map(int, input().split())
    pillar_pos.append((x, y))
    pillar_set.add((x, y))

res = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        a = pillar_pos[i]
        b = pillar_pos[j]
        ab = (b[0] - a[0], b[1] - a[0])
        ad1 = (-ab[1], ab[0])
        d1 = (ad1[0] + a[0], ad1[1] + a[1])
        c1 = (ad1[0] + b[0], ad1[1] + b[1])
        if d1 in pillar_set and c1 in pillar_set:
            res = max(res, ab[0] ** 2 + ab[1] ** 2)
            continue
        ad2 = (ab[1], -ab[0])
        d2 = (ad2[0] + a[0], ad2[1] + a[1])
        c2 = (ad2[0] + b[0], ad2[1] + b[1])
        if d2 in pillar_set and c2 in pillar_set:
            res = max(res, ab[0] ** 2 + ab[1] ** 2)

print(res)
