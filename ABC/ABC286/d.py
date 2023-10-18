# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, x = map(int, input().split())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

dp = [[0]*(x+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(x+1):
        if dp[i][j] == 0:
            continue
        for k in range(b[i]+1):
            if j+a[i]*k <= x:
                dp[i+1][j+a[i]*k] = 1
            else:
                break

if dp[n][x]:
    print("Yes")
else:
    print("No")
