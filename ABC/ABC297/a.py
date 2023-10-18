# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, d = map(int, input().split())
t = list(map(int, input().split()))

for i in range(n-1):
    if t[i+1] - t[i] <= d:
        print(t[i+1])
        break
else:
    print(-1)
