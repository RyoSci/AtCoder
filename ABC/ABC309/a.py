# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a, b = map(int, input().split())

if a % 3 == 0:
    print("No")
else:
    if a + 1 == b:
        print("Yes")
    else:
        print("No")
