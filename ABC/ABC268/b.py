# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()
t = input()

n = len(s)
m = len(t)

if n <= m:
    if s == t[:n]:
        print("Yes")
    else:
        print("No")
else:
    print("No")
