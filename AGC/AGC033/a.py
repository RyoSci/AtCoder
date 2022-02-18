from queue import Queue as Q
import time
tik = time.time()
# h, w = map(int, input().split())
h, w = 1000, 1000
a = [["." for i in range(w)] for j in range(h)]
a[0][0] = "#"
a[h - 1][0] = "#"
a[0][w - 1] = "#"
a[h - 1][w - 1] = "#"

# a = [["." for i in range(w)] for j in range(h)]
q = Q()

for i in range(h):
    # aij = input()
    aij = a[i]
    for j in range(w):
        if aij[j] == "#":
            q.put([i, j, 0])
        a[i][j] = aij[j]

res = 0
nwse = [[-1, 0], [0, -1], [1, 0], [0, 1]]
while not q.empty():
    x, y, n = q.get()
    for i, j in nwse:
        if 0 <= x + i <= h - 1 and 0 <= y + j <= w - 1 and a[x + i][y + j] == ".":
            a[x + i][y + j] = "#"
            q.put([x + i, y + j, n + 1])
            res = max(res, n + 1)

print(res)
print(time.time() - tik)
