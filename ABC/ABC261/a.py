# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

l1, r1, l2, r2 = map(int, input().split())
c = [0]*110
for i in range(l1, r1+1):
    c[i] += 1

for i in range(l2, r2+1):
    c[i] += 1

l = INF
r = -1
for i in range(110):
    if c[i] == 2:
        l = min(l, i)
        r = max(r, i)

if l == INF:
    print(0)
else:
    print(r-l)
