from itertools import combinations
import copy

h, w = map(int, input().split())
a = [list(input()) for i in range(h)]

ans = "Impossible"
total_proceed = [str(i) for i in range(h + w - 2)]
for i in combinations(total_proceed, h - 1):
    trace = [["." for j in range(w)] for _ in range(h)]
    xy = [0, 0]
    trace[xy[0]][xy[1]] = "#"
    for j in range(h + w - 2):
        if str(j) in i:
            xy[0] += 1
        else:
            xy[1] += 1
        trace[xy[0]][xy[1]] = "#"

    if trace == a:
        ans = "Possible"
        break

print(ans)
