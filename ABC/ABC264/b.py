# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

r, c = map(int, input().split())
g = [[0]*15 for _ in range(15)]

for i in range(15):
    if i % 2 == 0:
        for j in range(i, 15-i):
            g[j][i] = 1
        for j in range(i, 15-i):
            g[i][j] = 1
    else:
        for j in range(i, 15-i):
            g[i][j] = 0
        for j in range(i, 15-i):
            g[j][j] = 0

if r > 7:
    r = 15-r+1
if c > 7:
    c = 15-c+1

if g[r-1][c-1]:
    print("black")
else:
    print("white")

# print(*g, sep="\n")
