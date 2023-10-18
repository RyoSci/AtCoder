# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from itertools import permutations
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18


c = []
for i in range(3):
    ci = list(map(int, input().split()))
    c = c+ci


def f(p0, p1, now):
    if p0 == -1 or p1 == -1:
        return False
    if p0 == p1 and p1 != now:
        return True
    return False


ans = 0
for root in permutations(range(9)):
    g = [-1]*9
    flag = True
    for i in range(9):
        now = root[i]
        g[now] = c[now]

        # 縦
        p0 = g[(now+3) % 9]
        p1 = g[(now+6) % 9]
        if f(p0, p1, c[now]):
            flag = False
            break

        # 横
        if now % 3 == 0:
            p0 = g[(now+1) % 9]
            p1 = g[(now+2) % 9]
            if f(p0, p1, c[now]):
                flag = False
                break
        elif now % 3 == 1:
            p0 = g[(now-1) % 9]
            p1 = g[(now+1) % 9]
            if f(p0, p1, c[now]):
                flag = False
                break
        elif now % 3 == 2:
            p0 = g[(now-2) % 9]
            p1 = g[(now-1) % 9]
            if f(p0, p1, c[now]):
                flag = False
                break

        # 斜め右下
        if now in {0, 4, 8}:
            tmp = {0, 4, 8} - {now}
            tmp = list(tmp)
            p0 = g[tmp[0]]
            p1 = g[tmp[1]]
            if f(p0, p1, c[now]):
                flag = False
                break

        # 斜め右下
        if now in {2, 4, 6}:
            tmp = {2, 4, 6} - {now}
            tmp = list(tmp)
            p0 = g[tmp[0]]
            p1 = g[tmp[1]]
            if f(p0, p1, c[now]):
                flag = False
                break

    if flag:
        ans += 1


den = 1
for i in range(1, 10):
    den *= i

print(ans/den)
