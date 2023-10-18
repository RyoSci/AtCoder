# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, d = map(int, input().split())
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)


q = deque()

ans = [0]*n
q.append(0)
ans[0] = 1

while len(q):
    i = q.pop()

    for j in range(n):
        dis = (x[i]-x[j])**2 + (y[i]-y[j])**2
        if dis <= d**2:
            if ans[j] == 0:
                q.append(j)
            ans[j] = 1

for i in range(n):
    if ans[i]:
        print("Yes")
    else:
        print("No")
