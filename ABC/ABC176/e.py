# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w, m = list(map(int, input().split()))
hw = [list(map(int, input().split())) for _ in range(m)]
# m = 3*10**5
# hw = []
# for i in range(m):
#     hw.append([i+1, 1])
#     # hw.append([1, i+1])
h, w = zip(*hw)

d = dict()
for i in range(m):
    d[(h[i], w[i])] = 1

n = 3*10**5+10
# 各hiに対してwiがどれくらいいるかを管理
hs = [0]*n
for i in range(m):
    hs[h[i]] += 1

max_h = max(hs)
hss = []
for i in range(n):
    if hs[i] == max_h:
        hss.append(i)

# 各wiに対してhiがどれくらいいるかを管理
ws = [0]*n
for i in range(m):
    ws[w[i]] += 1

max_w = max(ws)
wss = []
for i in range(n):
    if ws[i] == max_w:
        wss.append(i)

ans = 0
for i in hss:
    for j in wss:
        if (i, j) in d:
            ans = max_h+max_w-1
        else:
            ans = max_h+max_w
            print(ans)
            exit()

print(ans)
