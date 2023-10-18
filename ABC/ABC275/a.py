# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
h = list(map(int, input().split()))

ans = 0
for i in range(n):
    if h[i] > h[ans]:
        ans = i

print(ans+1)
