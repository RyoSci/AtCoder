# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())

for i in range(h):
    ai = list(map(int, input().split()))
    si = ""
    for aij in ai:
        if aij == 0:
            si += "."
        else:
            si += chr(ord("A")+aij-1)
    print(si)
