from bisect import bisect_left, bisect_right
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


l, q = map(int, input().split())

# 座標圧縮
p = dict()
# 先頭と区切り位置を代表にする
p[0] = 0
cut = []
querry = []

for i in range(q):
    c, x = map(int, input().split())
    querry.append([c, x])
    p[x] = x
    if c == 1:
        cut.append(x)

cut = cut+[0, l]
cut.sort()
l = []
for i in range(len(cut)-1):
    l.append(cut[i+1]-cut[i])

# c = 2の時 x の親を手前の代表にする
# c = 1の時は長さの負を入れる
ps = sorted(list(p.keys()))
now = 0
for ci in range(len(cut)):
    while now < len(ps):
        if ps[now] == cut[ci]:
            p[ps[now]] = -l[ci]
        elif ps[now] < cut[ci]:
            p[ps[now]] = cut[ci-1]
        else:
            break
        now += 1


def find(x):
    if p[x] < 0:
        return x
    p[x] = find(p[x])
    return p[x]


def union(x, y):
    px = find(x)
    py = find(y)
    p[px] += p[py]
    p[py] = px
    return


# クエリを逆順に見ていく
querry = querry[::-1]
ans = []
for i in range(q):
    c, x = querry[i]
    if c == 1:
        a = bisect_left(cut, x)
        union(cut[a-1], cut[a])
    else:
        ans.append(-p[find(x)])

print(*ans[::-1], sep="\n")
