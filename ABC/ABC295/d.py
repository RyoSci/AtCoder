# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()
n = len(s)

tot = [[0]*(n+1) for _ in range(10)]

for i in range(n):
    si = int(s[i])
    tot[si][i+1] += 1

for i in range(10):
    for j in range(n):
        tot[i][j+1] += tot[i][j]

d = [0] * (1 << 11)
for j in range(n+1):
    mask = 0
    for i in range(10):
        if tot[i][j] % 2 == 1:
            mask <<= 1
            mask |= 1
        else:
            mask <<= 1
    d[mask] += 1

ans = 0
for i in range(1 << 11):
    ans += d[i]*(d[i]-1) // 2

print(ans)
