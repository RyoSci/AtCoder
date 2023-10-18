# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
p = list(map(int, input().split()))

dis = [0]*n
for i in range(n):
    tmp = (i+1)-p[i]
    tmp %= n
    dis[tmp] += 1

ans = 0
for i in range(2*n):
    tmp = dis[(i-1) % n] + dis[i % n] + dis[(i+1) % n]
    ans = max(ans, tmp)

print(ans)
