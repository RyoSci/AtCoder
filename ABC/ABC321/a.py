# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = input()
m = len(n)
if m == 1:
    print("Yes")
    exit()

for i in range(m-1):
    if int(n[i]) <= int(n[i+1]):
        print("No")
        exit()
else:
    print("Yes")
