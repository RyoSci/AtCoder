# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18
MOD = 998244353

n, m = map(int, input().split())
a, b, c, d, e, f = map(int, input().split())

NGs = set()
for i in range(m):
    xi, yi = map(int, input().split())
    NGs.add((xi, yi))


pre = dict()
pre[(0, 0)] = 1
for i in range(n):
    nxt = dict()
    for (x, y), cnt in pre.items():
        for dx, dy in zip([a, c, e], [b, d, f]):
            nx = x+dx
            ny = y+dy
            if (nx, ny) not in NGs:
                if (nx, ny) not in nxt:
                    nxt[(nx, ny)] = 0
                nxt[(nx, ny)] += cnt
                nxt[(nx, ny)] %= MOD
    pre = nxt

ans = 0
for _, cnt in nxt.items():
    ans += cnt
    ans %= MOD

print(ans)
