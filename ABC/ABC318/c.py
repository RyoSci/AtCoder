# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, d, p = map(int, input().split())
f = list(map(int, input().split()))
f.sort(reverse=True)

now = 0
tot = 0
for i in range(n):
    now += f[i]
    if i % d == d-1:
        tot += min(now, p)
        now = 0

tot += min(now, p)
print(tot)
