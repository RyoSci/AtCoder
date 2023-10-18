# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

same = 0
ans = 0
for i in range(n):
    if a[i] == i+1:
        same += 1
    else:
        j = a[i]-1
        if a[j] == i+1 and i < j:
            ans += 1

ans += same*(same-1)//2
print(ans)
