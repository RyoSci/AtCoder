# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()
m = 0
b = 0
for i in s:
    if i == "o":
        m += 1
    elif i == "x":
        b += 1

if m > 0 and b == 0:
    print("Yes")
else:
    print("No")
