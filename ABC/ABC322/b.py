# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
s = input()
t = input()

a = s == t[:n]
b = s == t[-n:]

if a and b:
    print(0)
elif a:
    print(1)
elif b:
    print(2)
else:
    print(3)
