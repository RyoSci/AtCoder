# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())

ans = INF
for a in range(1, n+1):
    b = (m+a-1)//a

    if b < a:
        break

    if m <= a * b and b <= n:
        ans = min(ans, a*b)

if ans == INF:
    print(-1)
else:
    print(ans)
