# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
# n = 2*10**5
# a = [_+1 for _ in range(n)]

ans = 0
x = 0
for i in range(n):
    if i+1 == a[i]:
        x += 1

    else:
        if a[a[i]-1] == i+1:
            ans += 1

ans //= 2
ans += x*(x-1)//2
print(ans)
