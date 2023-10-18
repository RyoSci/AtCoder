# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from itertools import permutations
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
grid = [[INF]*(n) for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1

    grid[a][b] = c
    grid[b][a] = c


ans = 0
for root in permutations(range(n)):
    now = 0
    for i in range(n-1):
        a = root[i]
        b = root[i+1]

        if grid[a][b] != INF:
            now += grid[a][b]
        else:
            break

    ans = max(ans, now)

print(ans)
