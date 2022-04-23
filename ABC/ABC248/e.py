# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)


if k == 1:
    print("Infinity")
    exit()


ans = set()

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dx = x[i]-x[j]
        dy = y[i]-y[j]
        cnt = []
        # 本番では場合わけしたが不要
        # if dx == 0:
        #     for kk in range(n):
        #         if x[kk] == x[i]:
        #             cnt.append(kk)
        #     if len(cnt) >= k:
        #         cnt.sort()
        #         ans.add((cnt[0], cnt[1]))
        # elif dy == 0:
        #     for kk in range(n):
        #         if y[kk] == y[i]:
        #             cnt.append(kk)
        #     if len(cnt) >= k:
        #         cnt.sort()
        #         ans.add((cnt[0], cnt[1]))
        # else:
        dxb = dx*y[i] - dy*x[i]
        for kk in range(n):
            if dx*y[kk] == dy*x[kk]+dxb:
                cnt.append(kk)
        if len(cnt) >= k:
            cnt.sort()
            ans.add((cnt[0], cnt[1]))

print(len(ans))
