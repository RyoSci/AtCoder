# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
# if __file__ != 'prog.py':
#     sys.setrecursionlimit(10 ** 7)
# input=lambda: sys.stdin.readline().rstrip()
INF = 10**18

n = int(input())
l = 1
r = n

while l+1 < r:
    m = (l+r)//2

    print(f"? {m}", flush=True)

    sm = int(input())

    if sm == 0:
        l = m
    else:
        r = m

print(f"! {l}", flush=True)
