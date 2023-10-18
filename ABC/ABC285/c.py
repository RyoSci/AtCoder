# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()
n = len(s)

ans = 0
now = 1
for i in range(n-1, -1, -1):
    tmp = ord(s[i])-ord("A")+1
    ans += tmp*now
    now *= 26

print(ans)
