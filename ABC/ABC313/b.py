# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
p = [0]*n
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    p[b] += 1


if p.count(0) == 1:
    for i in range(n):
        if p[i] == 0:
            print(i+1)

else:
    print(-1)
