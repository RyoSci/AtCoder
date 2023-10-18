# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

tot = sum(a)
cnt = n

ans = 0
for i in range(n):
    cnt -= 1
    tot -= a[i]
    ans += a[i]*cnt-tot

print(ans)
