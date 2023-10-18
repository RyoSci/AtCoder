# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
d = set()

for i in range(n):
    s = input()

    if s in d or s[::-1] in d:
        pass
    else:
        d.add(s)

print(len(d))
