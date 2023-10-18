# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
c = list(map(str, input().split()))
d = list(map(str, input().split()))
p = list(map(int, input().split()))

d2p = dict()

for i in range(m):
    d2p[d[i]] = p[i+1]

ans = 0
for i in range(n):
    if c[i] not in d2p:
        ans += p[0]
    else:
        ans += d2p[c[i]]

print(ans)
