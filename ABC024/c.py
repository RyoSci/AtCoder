n, d, k = map(int, input().split())
l_r = [list(map(int, input().split())) for i in range(d)]

for i in range(k):
    s, t = map(int, input().split())
    for j in range(d):
        l, r = l_r[j]
        if not l <= s <= r:
            continue
        else:
            if l <= t <= r:
                print(j + 1)
                break
            elif t < l:
                s = l
            else:
                s = r
