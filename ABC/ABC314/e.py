# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
c = []
p = []
s = []

for i in range(n):
    ci, pi, *si = list(map(int, input().split()))
    c.append(ci)
    p.append(pi)
    s.append(si)


E = [INF]*(m+1)
E[0] = 0

for k in range(1, m+1):
    for i in range(n):
        now = 0
        z = 0
        for j in range(p[i]):
            if s[i][j]:
                now += (E[max(0, k-s[i][j])]+c[i])/p[i]
            else:
                z += 1
        if z:
            now += (z*c[i])/p[i]
            z /= p[i]
            now /= (1-z)

        E[k] = min(E[k], now)


print(E[m])
