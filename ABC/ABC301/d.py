# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = list(input())
n = int(input())
m = len(s)

s = s[::-1]
now = 0
two = 1
for i in range(m):
    if s[i] == "?":
        pass
    else:
        now += two*int(s[i])
    two *= 2

s = s[::-1]
for i in range(m):
    two //= 2
    if s[i] == "?":
        if now + two <= n:
            now += two


if now <= n:
    print(now)
else:
    print(-1)
