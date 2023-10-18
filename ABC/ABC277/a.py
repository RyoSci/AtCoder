# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, x = map(int, input().split())
p = list(map(int, input().split()))

for i in range(n):
    if p[i] == x:
        print(i+1)
