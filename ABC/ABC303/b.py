# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())

cor = [[1]*n for _ in range(n)]

for i in range(m):
    ai = list(map(lambda x: int(x)-1, input().split()))

    for j in range(n-1):
        cor[ai[j]][ai[j+1]] = 0
        cor[ai[j+1]][ai[j]] = 0

ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue

        ans += cor[i][j]

print(ans//2)
