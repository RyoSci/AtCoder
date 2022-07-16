# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m, x, t, d = list(map(int, input().split()))

tall = [0]*(n+1)
for i in range(n, x-1, -1):
    tall[i] = t

for i in range(x-1, -1, -1):
    tall[i] = tall[i+1]-d

print(tall[m])
