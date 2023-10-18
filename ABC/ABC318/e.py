# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

d = [[] for _ in range(n+1)]

for i in range(n):
    d[a[i]].append(i)

ans = 0
for i in range(n+1):
    if len(d[i]) < 2:
        continue

    l = d[i][0]
    tot = 0
    for r in range(1, len(d[i])):
        dis = d[i][r] - d[i][r-1]-1
        tot += (r-1+1) * (len(d[i]) - r) * dis

    ans += tot

print(ans)
