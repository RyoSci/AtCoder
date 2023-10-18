# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

dp = [[0]*200 for _ in range(n+1)]
p = [[[] for i in range(200)] for j in range(n+1)]


dp[0][0] = 1
for i in range(n):
    for j in range(200):
        if dp[i][j] == 0:
            continue
        # 何もしない
        dp[i+1][j] += dp[i][j]
        p[i+1][j].append(j)

        # 足す
        dp[i+1][(j+a[i]) % 200] += dp[i][j]
        if a[i] % 200 == 0:
            p[i+1][(j+a[i]) % 200].append(j-200)
        else:
            p[i+1][(j+a[i]) % 200].append(j)

for i in range(200):
    if i == 0 and dp[n][i] >= 3 or i > 0 and dp[n][i] >= 2:
        ans = "Yes"
        print(ans)
        ii = i
        now = ii
        b = []
        for i in range(n, 0, -1):
            # print(p[i][now])
            if p[i][now][0] != now:
                b.append(i)
            now = p[i][now][0]
            now %= 200

        print(len(b), *b[::-1])
        now = ii
        c = []
        for i in range(n, 0, -1):
            # print(p[i][now])
            if p[i][now][-1] != now:
                c.append(i)

            now = p[i][now][-1]
            now %= 200

        print(len(c), *c[::-1])
        break
else:
    ans = "No"
    print(ans)
