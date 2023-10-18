# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, a, b = map(int, input().split())
s = input()

ans = INF
for i in range(n):
    res = a*i
    for j in range(n//2):
        if s[j] != s[n-1-j]:
            res += b
    ans = min(ans, res)
    s = s[1:] + s[0]

print(ans)
