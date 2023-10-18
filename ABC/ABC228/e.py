# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k, m = map(int, input().split())
mod = 998244353

if m % mod == 0:
    print(0)
else:
    a = pow(k, n, mod-1)
    b = pow(m, a, mod)
    print(b)
