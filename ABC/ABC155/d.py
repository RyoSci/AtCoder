# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

# n, k = map(int, input().split())
# a = list(map(int, input().split()))
n, k = 2*10**5, 2*10**8
a = []
for i in range(n//2):
    a.append(10**9-i)
for i in range(n//2, n):
    a.append(-10**9+i)
a.sort()

b = [-a[i] for i in range(n-1, -1, -1)]
# ok = -INF
# ng = INF
ok = min(a[0]*a[-1], a[0]*a[1], a[-1]*a[-2])
ng = max(a[-1]*a[-2], a[0]*a[1])
# ok = -10
# ng = 10


# def f(m):
#     # ai*aj<m となる数を数える
#     cnt = 0
#     for i in range(n):
#         ai = a[i]
#         if ai == 0:
#             if 0 < m:
#                 cnt += n

#         elif ai > 0:
#             aj = (m+ai-1)//ai
#             tmp = bisect_left(a, aj)
#             cnt += tmp
#         else:
#             ai *= -1
#             aj = (m+ai-1)//ai
#             tmp = bisect_left(b, aj)
#             cnt += tmp

#         if ai*ai < m:
#             cnt -= 1
#     return cnt//2 < k


while ok+1 < ng:
    m = (ok+ng)//2

    # ai*aj<m となる数を数える
    cnt = 0
    for i in range(n):
        ai = a[i]
        if ai == 0:
            if 0 < m:
                cnt += n

        elif ai > 0:
            if m >= 0:
                aj = (m+ai-1)//ai
            else:
                aj = (m+ai+1)//ai

            tmp = bisect_left(a, aj)
            cnt += tmp
        else:
            ai *= -1
            if m >= 0:
                aj = (m+ai-1)//ai
            else:
                aj = (m+ai+1)//ai
            tmp = bisect_left(b, aj)
            cnt += tmp

        if ai*ai < m:
            cnt -= 1

    if cnt//2 < k:
        ok = m
    else:
        ng = m
    # if f(m):
    #     ok = m
    # else:
    #     ng = m

print(ok)
