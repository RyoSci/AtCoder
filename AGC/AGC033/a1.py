h, w = map(int, input().split())
a = [input() for _ in range(h)]

dis_black2origin = set()
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            dis_black2origin.add(i + j)

dis_black2origin = sorted(list(dis_black2origin))


def binary_search(dis):
    l = 0
    r = len(dis_black2origin) - 1
    m = (l + r) // 2
    while l + 1 != r:
        if dis == dis_black2origin[m]:
            return 0
        elif dis < dis_black2origin[m]:
            r = m
            m = (l + r) // 2
        else:
            l = m
            m = (l + r) // 2
    res = min(abs(dis_black2origin[l] - dis), abs(dis_black2origin[r] - dis))
    return res


ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            continue
        ans = max(ans, binary_search(i + j))

print(ans)
