# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, a, b = map(int, input().split())
c = list(map(int, input().split()))

for i in range(n):
    if a+b == c[i]:
        print(i+1)
        break
