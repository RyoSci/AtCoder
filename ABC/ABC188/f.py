# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import defaultdict
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

x, y = map(int, input().split())


memo = defaultdict(int)


def f(y):
    if y in memo:
        return memo[y]
    if y == 1:
        return abs(x-y)

    if y % 2 == 0:
        memo[y] = min(f(y//2)+1, abs(x-y))
    else:
        memo[y] = min(f(y+1)+1, f(y-1)+1, abs(x-y))

    return memo[y]


ans = f(y)

print(ans)
