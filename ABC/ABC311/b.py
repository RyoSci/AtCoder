# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, d = map(int, input().split())
s = []
for i in range(n):
    si = input()
    s.append(list(si))

ans = 0
now = 0
for j in range(d):
    flag = True
    for i in range(n):
        if s[i][j] == "x":
            flag = False

    if flag:
        now += 1
        ans = max(ans, now)
    else:
        now = 0

print(ans)
