# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = list(input())
n = len(s)

for i in range(n//2):
    s[2*i], s[2*i+1] = s[2*i+1], s[2*i]

print("".join(s))
