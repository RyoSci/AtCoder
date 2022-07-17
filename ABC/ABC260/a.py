# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input=lambda: sys.stdin.readline().rstrip()
INF = 10**18

s = list(input())
s.sort()

if s[0]==s[1] and s[1]==s[2]:
    print(-1)
elif s[0]==s[1]:
    print(s[2])
else:
    print(s[0])