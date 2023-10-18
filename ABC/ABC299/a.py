# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()

a = []
b = []
for i in range(n):
    if s[i] == '|':
        a.append(i)
    elif s[i] == '*':
        b.append(i)

if a[0] <= b[0] <= a[1]:
    print("in")
else:
    print("out")
