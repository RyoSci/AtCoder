# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()

t = ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"]

if s in t:
    print("Yes")
else:
    print("No")
