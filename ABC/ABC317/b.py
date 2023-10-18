# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)
input=lambda: sys.stdin.readline().rstrip()
INF = 10**18

n = int(input())
a = list(map(int, input().split()))
a.sort()

for i in range(a[0], a[-1]):
    if i not in a:
        print(i)
        break