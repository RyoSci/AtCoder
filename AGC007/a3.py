h, w = map(int, input().split())
a = [list(input()) for i in range(h)]

ans = "Impossible"
total_proceed = [str(i) for i in range(h + w - 2)]

for i in range(1 << (h + w - 2)):
    down = []
    for j in range(h + w - 2):
        if i >> j & 1:
            down.append(j)
    if len(down) == h - 1:
        trace = [["." for j in range(w)] for _ in range(h)]
        xy = [0, 0]
        trace[xy[0]][xy[1]] = "#"
        for j in range(h + w - 2):
            if j in down:
                xy[0] += 1
            else:
                xy[1] += 1
            trace[xy[0]][xy[1]] = "#"
        if trace == a:
            ans = "Possible"
            break

print(ans)
