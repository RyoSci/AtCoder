# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

q = int(input())

ans = 1
mod = 998244353

top = deque()
top.append(1)

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]
        ans *= 10
        ans += x
        ans %= mod

        top.append(x)

    elif query[0] == 2:
        now = top.popleft()
        d = len(top)
        ans -= now*pow(10, d, mod)
        ans %= mod

    else:
        print(ans)
