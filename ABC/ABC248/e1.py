# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from fractions import Fraction
from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)


if k == 1:
    print("Infinity")
    exit()


lines = dict()
# lines = defaultdict(int)

for i in range(n-1):
    for j in range(i+1, n):
        dx = x[i]-x[j]
        dy = y[i]-y[j]
        if dx == 0:
            if x[i] not in lines:
                lines[x[i]] = 0
            lines[x[i]] += 1
        else:
            a = Fraction(dy, dx)
            b = y[i]-a*x[i]
            if (a, b) not in lines:
                lines[(a, b)] = 0
            lines[(a, b)] += 1

ans = 0
for val in lines.values():
    if val >= k*(k-1)//2:
        ans += 1

print(ans)
