# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()

for i in range(n-2):
    t = s[i:i+3]
    if t == "ABC":
        print(i+1)
        break
else:
    print(-1)
