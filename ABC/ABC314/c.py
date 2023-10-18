# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
s = input()
c = list(map(int, input().split()))

g = [[] for _ in range(m)]
for i in range(n):
    g[c[i]-1].append(i)

for i in range(m):
    tmp = g[i].pop()
    g[i] = [tmp] + g[i]

cnt = [0]*m
ans = ""
for i in range(n):
    ans += s[g[c[i]-1][cnt[c[i]-1]]]
    cnt[c[i]-1] += 1

print(ans)
