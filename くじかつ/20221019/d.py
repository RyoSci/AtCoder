# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

g = [[0]*10 for _ in range(10)]

for i in range(1, n+1):
    s = str(i)
    g[int(s[0])][int(s[-1])] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += g[i][j]*g[j][i]

print(ans)
