# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

t = int(input())
for _ in range(t):
    n, m, sx, sy, d = map(int, input().split())
    sx -= 1
    sy -= 1

    flag0 = True
    for j in range(m):
        x, y = 0, j
        dx = abs(sx-x)
        dy = abs(sy-y)
        if dx+dy <= d:
            flag0 = False
            break

    for i in range(n):
        x, y = i, m-1
        dx = abs(sx-x)
        dy = abs(sy-y)
        if dx+dy <= d:
            flag0 = False
            break

    flag1 = True
    for i in range(n):
        x, y = i, 0
        dx = abs(sx-x)
        dy = abs(sy-y)
        if dx+dy <= d:
            flag1 = False
            break

    for j in range(m):
        x, y = n-1, j
        dx = abs(sx-x)
        dy = abs(sy-y)
        if dx+dy <= d:
            flag1 = False
            break

    if flag0 or flag1:
        print(n+m-2)
    else:
        print(-1)
