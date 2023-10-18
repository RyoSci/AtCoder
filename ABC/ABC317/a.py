# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)
input=lambda: sys.stdin.readline().rstrip()
INF = 10**18

n, h, x = map(int, input().split())
p = list(map(int, input().split()))

for i in range(n):
    if h+p[i]>=x:
        print(i+1)
        exit()