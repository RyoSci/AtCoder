# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
d = set()
e = []
for i in range(n):
    s, t = input().split()
    t = int(t)
    if s not in d:
        d.add(s)
        e.append([t, -i])

e.sort(reverse=True)
print(-e[0][1]+1)
