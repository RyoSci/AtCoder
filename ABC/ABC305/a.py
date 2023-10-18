# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
if abs(n-n//5*5) > abs(n-(n+5-1)//5*5):
    print((n+5-1)//5*5)
else:
    print(n//5*5)
