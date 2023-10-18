# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left
from math import atan2, pi
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
x, y = zip(*xy)


def rad2deg(x):
    res = x * 180/pi
    res %= 360
    return res


ans = 0
for i in range(n):
    lines = []
    for j in range(n):
        if i == j:
            continue
        dx = x[j]-x[i]
        dy = y[j]-y[i]
        sita = atan2(dy, dx)
        lines.append(sita)
        sita = 2*pi+sita
        lines.append(sita)

    lines.sort()
    for j in range(len(lines)):
        now = lines[j]
        pos = bisect_left(lines, now+pi)
        if pos == len(lines):
            continue
        # print(j, pos, now/pi*180, (now+pi)/pi*180, lines[pos]/pi*180)
        a = rad2deg(lines[pos]) - rad2deg(now)
        b = rad2deg(lines[pos-1]) - rad2deg(now)
        a %= 360
        b %= 360
        # print(a, b)
        a = min(a, 360-a)
        b = min(b, 360-b)
        ans = max(ans, a,  b)


print(ans)
