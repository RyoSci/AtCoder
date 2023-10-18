# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, t = map(str, input().split())

n = int(n)
lt = len(t)
t = list(t)

s = []
for i in range(n):
    s.append(list(input()))

dist = [[[0]*(1) for j in range(n)] for i in range(2)]


for inv in range(2):
    for pos in range(n):

        i = 0
        j = 0

        si = s[pos]
        lsi = len(si)
        cnt = 0

        while i < lt and j < lsi:
            if t[i] == si[j]:
                cnt += 1
                i += 1
                j += 1
                dist[inv][pos].append(cnt)
            else:
                j += 1
        s[pos] = s[pos][::-1]
    t = t[::-1]

k = 10**6
a = [0]*k
b = [0]*k

for inv in range(2):
    for i in range(n):
        if inv:
            for j in dist[inv][i]:
                b[j] += 1
        else:
            for j in dist[inv][i]:
                a[j] += 1

ans = 0
# print(a[:10])
# print(b[:10])
# print(dist)
for i in range(n):
    tmp = dist[0][i]
    tmp1 = dist[1][i]

    # 前後
    aa = 0
    for j in tmp:
        aa = max(aa, b[lt-j])
    ans += aa

    # 後前
    bb = 0
    for j in tmp1:
        bb = max(bb, a[lt-j])
    ans += bb


print(ans//2)
