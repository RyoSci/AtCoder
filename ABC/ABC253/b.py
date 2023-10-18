# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())

s = [input() for _ in range(h)]

x = []
y = []
for i in range(h):
    for j in range(w):
        if s[i][j] == "o":
            x.append(i)
            y.append(j)

print(abs(x[0]-x[1])+abs(y[0]-y[1]))
