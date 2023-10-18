# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18


g = [[0]*(101) for _ in range(101)]
n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())
    for j in range(a, b):
        for k in range(c, d):
            g[j][k] += 1

ans = 0
for i in range(101):
    for j in range(101):
        if g[i][j] > 0:
            ans += 1

print(ans)
