# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from itertools import permutations
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, c = map(int, input().split())
d = []
for i in range(c):
    di = list(map(int, input().split()))
    d.append(di)

g = []
mod = [[0]*c for _ in range(3)]
for i in range(n):
    gi = list(map(int, input().split()))
    g.append(gi)
    for j in range(n):
        mod[(i+1+j+1) % 3][g[i][j]-1] += 1

ans = INF
for i in permutations(range(c), 3):
    cnt = 0
    for j in range(3):
        x = i[j]
        for k in range(c):
            cnt += d[k][x]*mod[j][k]

    # print(cnt)
    ans = min(ans, cnt)


print(ans)
