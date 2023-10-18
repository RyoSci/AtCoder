# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
s = []
for i in range(n):
    si = input()
    s.append(si)

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        solve = [0]*m
        for k in range(m):
            if s[i][k] == "o" or s[j][k] == "o":
                solve[k] = 1
        if sum(solve) == m:
            ans += 1
print(ans)
