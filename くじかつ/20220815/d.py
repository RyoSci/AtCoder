# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
# n = 2*10**5
# a = list(range(1, n+1))

m = 2*(10**5)+10
d = [0]*(m+1)
for i in range(n):
    d[a[i]] += 1

ans = 0
for aj in range(1, m):
    for ak in range(m//aj+1):
        ai = aj*ak
        if ai <= m:
            ans += d[ai]*d[aj]*d[ak]

print(ans)
