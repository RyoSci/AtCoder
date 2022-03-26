# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
a = a[::-1]
c = c[::-1]

b = [-1]*(m+1)
b[0] = c[0]//a[0]

for i in range(1, m+1):
    tmp = 0
    for j in range(1, i+1):
        if 0 <= j <= n and 0 <= i-j <= m:
            tmp += a[j]*b[i-j]
    b[i] = (c[i]-tmp)//a[0]

print(*b[::-1])
