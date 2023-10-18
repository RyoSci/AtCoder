# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

t = int(input())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


ans = []
for _ in range(t):
    n, d, k = map(int, input().split())
    k -= 1
    g = gcd(n, d)
    num = n//g
    cycle_cnt = k // num
    res = cycle_cnt + (k % num)*d
    ans.append(res % n)

print(*ans)
