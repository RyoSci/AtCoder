# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))

if t not in c:
    t = c[0]

ans = 0
pos = -1
for i in range(n):
    if c[i] != t:
        continue
    if ans < r[i]:
        ans = r[i]
        pos = i

print(pos+1)
