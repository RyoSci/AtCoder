# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
b = set(b)

x = int(input())

dp = [0]*(x+1)
dp[0] = 1

for i in range(x+1):
    if dp[i] == 0:
        continue

    for j in range(n):
        ni = i + a[j]
        if ni not in b and ni <= x:
            dp[ni] = dp[i]

if dp[x] == 1:
    print("Yes")
else:
    print("No")
