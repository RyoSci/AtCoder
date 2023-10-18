# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())
a = []
for i in range(h):
    ai = list(map(int, input().split()))
    a.append(ai)

ans = 0
seen = []


def dfs(x, y):
    global ans
    seen.append(a[x][y])
    if x == h-1 and y == w-1:
        if len(set(seen)) == h+w-1:
            ans += 1
    # 右
    if y < w-1:
        dfs(x, y+1)
    # 下
    if x < h-1:
        dfs(x+1, y)

    seen.pop()


dfs(0, 0)

print(ans)
