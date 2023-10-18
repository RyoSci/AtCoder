# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
# n = 10**18

d = dict()


def f(x):
    if x == 0:
        return 1
    if x in d:
        return d[x]
    d[x] = f(x//2) + f(x//3)
    return d[x]


print(f(n))
