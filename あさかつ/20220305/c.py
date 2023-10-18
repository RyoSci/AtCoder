# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
x = []
y = []
grid = dict()
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
    grid[(xi, yi)] = 1

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        dx = x[j]-x[i]
        dy = y[j]-y[i]
        if dx != 0 and dy != 0 and (x[i]+dx, y[i]) in grid and (x[i], y[i]+dy) in grid:
            ans += 1

print(ans//2)
