# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
x = []
y = []
p = []
for i in range(n):
    xi, yi, pi = list(map(int, input().split()))
    x.append(xi)
    y.append(yi)
    p.append(pi)


def f(m):
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if p[i]*m >= abs(x[i]-x[j])+abs(y[i]-y[j]):
                dp[i][j] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k]*dp[k][j] == 1:
                    dp[i][j] = 1

    for i in range(n):
        flag = True
        for j in range(n):
            if dp[i][j] == 0:
                flag = False
        if flag:
            return True
    return False


ok = 10**10
ng = 0
while ng+1 < ok:
    m = (ok+ng)//2
    if f(m):
        ok = m
    else:
        ng = m

print(ok)
