# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from itertools import permutations
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(lambda x:int(x)-1, input().split())) for _ in range(N)]

c_map = [[0]*C for _ in range(3)]
for i in range(N):
    for j in range(N):
        pos = (i+j) % 3
        c_tmp = c[i][j]
        c_map[pos][c_tmp] += 1

ans = INF

for i in permutations(range(C), 3):
    res = 0
    for j in range(3):
        for k in range(C):
            res += D[k][i[j]]*c_map[j][k]
    ans = min(ans, res)

print(ans)
