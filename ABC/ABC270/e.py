# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
a = list(map(int, input().split()))

ok = INF
ng = 0


def f(m):
    res = 0
    for i in range(n):
        res += min(a[i], m)
    return res


while ng+1 < ok:
    m = (ng+ok)//2
    if f(m) >= k:
        ok = m
    else:
        ng = m

rest = k-f(ng)
for i in range(n):
    a[i] = max(0, a[i]-ng)


for i in range(2*n):
    if a[i % n] > 0:
        a[i % n] -= 1
        rest -= 1

    if rest == 0:
        break

print(*a)
