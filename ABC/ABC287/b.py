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

t = set()
for i in range(m):
    ti = input()
    t.add(ti)

ans = 0
for i in range(n):
    if s[i][-3:] in t:
        ans += 1

print(ans)
