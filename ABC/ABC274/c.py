# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

ans = dict()
ans[1] = 0

for i in range(n):
    b = (i+1)*2
    c = (i+1)*2+1
    # print(b, c)
    ans[b] = ans[a[i]]+1
    ans[c] = ans[a[i]]+1

for i in range(2*n+1):
    print(ans[i+1])
