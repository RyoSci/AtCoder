# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)
input=lambda: sys.stdin.readline().rstrip()
INF = 10**18

n, p, q = map(int, input().split())
d = list(map(int, input().split()))

ans = min(p, q+min(d))
print(ans)