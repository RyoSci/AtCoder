# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input=lambda: sys.stdin.readline().rstrip()
INF = 10**18

s = input()

ans=-1
for i in range(len(s)):
    if s[i] == "a":
        ans=i+1

print(ans)