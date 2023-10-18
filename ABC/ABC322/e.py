# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k, p = map(int, input().split())
c = []
a = []

for i in range(n):
    ci, *ai = list(map(int, input().split()))
    c.append(ci)
    a.append(ai)

dp = dict()
tmp = tuple([0]*k)
dp[tmp] = 0

for i in range(n):
    nxt = dict()

    for key, val in dp.items():

        # 使わない
        if key not in nxt:
            nxt[key] = INF
        nxt[key] = min(nxt[key], val)

        # 使う
        tmp = [0]*k
        for j in range(k):
            tmp[j] += a[i][j]
            tmp[j] += key[j]
            tmp[j] = min(tmp[j], p)
        key = tuple(tmp)
        if key not in nxt:
            nxt[key] = INF
        nxt[key] = min(nxt[key], val+c[i])

    dp = nxt

tmp = [p]*k
tmp = tuple(tmp)

if tmp in dp:
    print(dp[tmp])
else:
    print(-1)
