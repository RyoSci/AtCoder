# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, x = map(int, input().split())
s = ""
for i in range(26):
    for j in range(n):
        s += chr(ord("A")+i)

print(s[x-1])
