# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
sx, sy, tx, ty = list(map(int, input().split()))

xyr = []

for i in range(n):
    xi, yi, ri = list(map(int, input().split()))
    xyr.append((xi, yi, ri))


def f(x, y, x1, y1, r):
    return (x-x1)**2+(y-y1)**2 == r**2


q = []
seen = [0]*n
for i in range(n):
    x, y, r = xyr[i]
    if f(sx, sy, x, y, r):
        q.append(i)
        seen[i] = 1

while len(q) != 0:
    bottom = q.pop()
    x, y, r = xyr[bottom]
    for i in range(n):
        nx, ny, nr = xyr[i]
        if (nr-r)**2 <= (nx-x)**2+(ny-y)**2 <= (nr+r)**2 and seen[i] == 0:
            q.append(i)
            seen[i] = 1

ans = "No"
for i in range(n):
    x, y, r = xyr[i]
    if seen[i]:
        if f(tx, ty, x, y, r):
            ans = "Yes"


print(ans)
# print(seen)
