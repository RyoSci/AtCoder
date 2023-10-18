# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w, c = map(int, input().split())
a = []
for i in range(h):
    ai = list(map(int, input().split()))
    a.append(ai)

ans = INF
for k in range(2):
    dp = [[INF]*(w) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            now = INF
            if i:
                now = min(now, dp[i-1][j])
            if j:
                now = min(now, dp[i][j-1])

            ans = min(ans, now+a[i][j]+c*(i+j))
            dp[i][j] = min(now, a[i][j] - c*(i+j))

    for i in range(h):
        a[i] = a[i][::-1]

print(ans)
