# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
p = list(map(lambda x: int(x)-1, input().split()))
p = [0]+p
par = n-1

ans = 0
while par > 0:
    par = p[par]
    ans += 1

print(ans)
