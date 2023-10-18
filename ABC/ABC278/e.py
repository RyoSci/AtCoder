# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

H, W, N, h, w = map(int, input().split())
a = []
d = dict()
for i in range(H):
    ai = list(map(int, input().split()))
    a.append(ai)
    for aij in ai:
        if aij not in d:
            d[aij] = 0
        d[aij] += 1

for i in range(h):
    for j in range(w):
        aij = a[i][j]
        d[aij] -= 1
        if d[aij] == 0:
            del d[aij]

HH = H-h+1
WW = W-w+1
ans = [[0]*WW for _ in range(HH)]
ans[0][0] = len(d)

for k in range(HH):
    for l in range(WW):
        if k > 0 and l == 0:
            d = pre
            # 下にスライド
            for j in range(l, l+w):
                if a[k-1][j] not in d:
                    d[a[k-1][j]] = 0
                d[a[k-1][j]] += 1

                d[a[k+h-1][j]] -= 1
                if d[a[k+h-1][j]] == 0:
                    del d[a[k+h-1][j]]

        if l == 0:
            # コピー
            pre = dict()
            for key, val in d.items():
                pre[key] = val

        else:
            # 横にスライド
            for i in range(k, k+h):
                if a[i][l-1] not in d:
                    d[a[i][l-1]] = 0
                d[a[i][l-1]] += 1

                d[a[i][l+w-1]] -= 1
                if d[a[i][l+w-1]] == 0:
                    del d[a[i][l+w-1]]

        ans[k][l] = len(d)

for i in range(HH):
    print(*ans[i])
