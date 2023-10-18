# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()

t = []

now = 0
for i in range(n):
    if s[i] == "-":
        t.append(now)
        now = 0
    else:
        now += 1

if now != 0:
    t.append(now)

ans = 0
for i in t:
    ans = max(ans, i)

if ans == 0 or "-" not in s:
    print(-1)
else:
    print(ans)
