# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from math import sqrt
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
x = []
y = []
xp = []
yq = []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
    xp.append(xi)
    yq.append(yi)

p = []
q = []
xp = []
yq = []
for i in range(m):
    pi, qi = map(int, input().split())
    p.append(pi)
    q.append(qi)
    xp.append(pi)
    yq.append(qi)

xp = [0]+p+x
yq = [0]+q+y

m += 1
l = n+m
dis = [[0]*l for _ in range(l)]
for i in range(l):
    for j in range(l):
        dis[i][j] = sqrt((xp[i]-xp[j])**2+(yq[i]-yq[j])**2)


dp = [[INF]*l for _ in range(1 << l)]

dp[0][0] = 0
for i in range(1 << l):
    boost = 0
    for j in range(1, m):
        if (i >> j) & 1:
            boost += 1

    if i == 0:
        for j in range(l):
            print("AA")
            for k in range(l):
                if j == k:
                    continue
                dp[i | (1 << k)][k] = min(dp[i | (1 << k)]
                                          [k], dp[i][j] + dis[j][k]/(1+boost))
    else:
        for j in range(l):
            if not ((i >> j) & 1):
                continue
            print("AAB")
            for k in range(l):
                if j == k:
                    continue
                dp[i | (1 << k)][k] = min(dp[i | (1 << k)]
                                          [k], dp[i][j] + dis[j][k]/(1+boost))
                print(i, j, k)

ans = INF
for i in range(1 << m):
    for j in range(l):
        ans = min(ans, dp[(1 << n) << m+i][0])

print(ans)
print(dp)
print(dis)
