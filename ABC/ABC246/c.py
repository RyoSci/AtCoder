# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k, x = list(map(int, input().split()))
a = list(map(int, input().split()))

for i in range(n):
    if a[i]//x >= 1:
        use = min(k, a[i]//x)
        a[i] = a[i]-use*x
        k -= use

a.sort(reverse=True)
if k > 0:
    k = min(k, n)
    for i in range(k):
        a[i] = 0

print(sum(a))
