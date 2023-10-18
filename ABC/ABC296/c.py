# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, x = map(int, input().split())
a = list(map(int, input().split()))

d = dict()
for i in range(n):
    if a[i] not in d:
        d[a[i]] = 0
    d[a[i]] += 1

ans = "No"
for i in range(n):
    if a[i] + x in d:
        ans = "Yes"
        break

print(ans)
