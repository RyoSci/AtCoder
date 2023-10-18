# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)
input=lambda: sys.stdin.readline().rstrip()
INF = 10**18

n, m, p = map(int, input().split())

ans = 0
for i in range(m, n+1, p):
    ans+=1

print(ans)