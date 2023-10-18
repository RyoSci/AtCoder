# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ab = []
for i in range(n):
    ab.append([max(0, -1+(a[i]/b[i])**0.5), i])

ab.sort()

ans = 0
for i in range(n):
    x, i = ab[i]
    ans += a[i]/(1+x)+b[i]*(1+x)

print(ans)
