# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

for i in range(8):
    s = input()
    for j in range(8):
        if s[j] == "*":
            print(chr(ord("a")+j) + str(8 - i))
