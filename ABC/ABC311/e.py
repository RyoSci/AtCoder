# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w, n = map(int, input().split())
a = []
b = []
grid = [[0]*(w+1) for _ in range(h+1)]
s = [[0]*(w+1) for _ in range(h+1)]
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

    grid[ai][bi] = 1
    s[ai][bi] = 1


for i in range(h):
    for j in range(w):
        grid[i+1][j+1] += grid[i+1][j] + grid[i][j+1] - grid[i][j]

# for i in range(h+1):
#     print(*grid[i])


def f(i, j, m):
    res = grid[i+m-1][j+m-1] - grid[i-1][j+m-1] - \
        grid[i+m-1][j-1] + grid[i-1][j-1]

    return res == 0


cnt = [0]*3010
for i in range(1, h+1):
    for j in range(1, w+1):

        if s[i][j]:
            continue
        ok = 1
        ng = 3010

        while ok + 1 < ng:
            m = (ok+ng)//2

            if i+m-1 < h+1 and j+m-1 < w+1 and f(i, j, m):
                ok = m
            else:
                ng = m

        cnt[ok] += 1

# print(*cnt[:10])
ans = 0
for i in range(3010):
    ans += cnt[i]*i

print(ans)
