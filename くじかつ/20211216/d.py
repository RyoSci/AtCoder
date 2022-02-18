from bisect import bisect_left
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
INF = 10**18
r, g, b = [-INF, INF], [-INF, INF], [-INF, INF]
for i in range(2*n):
    a, c = input().split()
    a = int(a)
    if c == "R":
        r.append(a)
    elif c == "G":
        g.append(a)
    elif c == "B":
        b.append(a)
r.sort()
g.sort()
b.sort()

ans = INF
if len(r) % 2 == 0 and len(g) % 2 == 0 and len(b) % 2 == 0:
    print(0)
else:
    if len(r) % 2 == 0:
        for i in g:
            index = bisect_left(b, i)
            ans = min(ans, abs(i-b[index]))
            ans = min(ans, abs(i-b[index-1]))
        tmp_g = []
        for i in g:
            index = bisect_left(a, i)
            tmp_g.append([abs(i-a[index]), index])
            index -= 1
            tmp_g.append([abs(i-a[index]), index])

        tmp_b = []
        for i in b:
            index = bisect_left(a, i)
            tmp_b.append([abs(i-a[index]), index])
            index -= 1
            tmp_b.append([abs(i-a[index]), index])

        tmp_g.sort()
        tmp_b.sort()

        if tmp_g[0][1] != tmp_b[0][1]:
            ans = min(ans, tmp_g[0][0]+tmp_b[0][0])
    #     else:

    # elif len(g)%2==0:

    # elif len(b)%2==0:
