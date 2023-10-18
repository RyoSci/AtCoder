# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, s = map(int, input().split())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

dp = [[0]*(s+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(s+1):
        if dp[i][j] == 0:
            continue
        if j+a[i] <= s:
            dp[i+1][j+a[i]] = dp[i][j]
        if j+b[i] <= s:
            dp[i+1][j+b[i]] = dp[i][j]

if dp[n][s] != 1:
    print("No")
else:
    ans = []
    j = s
    for i in range(n, 0, -1):
        ja = j-a[i-1]
        jb = j-b[i-1]

        if 0 <= ja and dp[i-1][ja] == 1:
            ans.append("H")
            j = ja
        elif 0 <= jb and dp[i-1][jb] == 1:
            ans.append("T")
            j = jb

    ans = ans[::-1]
    print("Yes")
    print("".join(ans))
