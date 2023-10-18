# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())
c = []
for i in range(h):
    ci = list(input())
    c.append(ci)

for i in range(h):
    for j in range(w):
        if c[i][j] == "S":
            sx = i
            sy = j
            break

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def check(i, j):
    return 0 <= i < h and 0 <= j < w and c[i][j] == "."


for i in range(4):
    sxi = sx+dx[i]
    syi = sy+dy[i]
    if not check(sxi, syi):
        continue

    q = deque()

    q.append([sxi, syi])
    seen = [[0]*w for _ in range(h)]
    seen[sxi][syi] = 1

    while len(q) > 0:
        nxi, nyi = q.popleft()
        # print(nxi, nyi, "aaa")
        for j in range(4):
            sxj = nxi+dx[j]
            syj = nyi+dy[j]
            if not check(sxj, syj):
                continue
            if seen[sxj][syj] == 0:
                seen[sxj][syj] = 1
                q.append([sxj, syj])

    # print(i, sxi, syi)
    # print(seen)

    for j in range(i+1, 4):
        sxj = sx+dx[j]
        syj = sy+dy[j]
        if not check(sxj, syj):
            continue
        if seen[sxj][syj]:
            print("Yes")
            exit()


print("No")
