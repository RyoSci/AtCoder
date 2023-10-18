# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
c = list(input())

d = sorted(c)
pos = -1
for i in range(n-1):
    if d[i] != d[i+1]:
        pos = i

if pos == -1:
    print(0)
else:
    ans = 0
    for i in range(pos+1):
        if c[i] == "W":
            ans += 1
    print(ans)
