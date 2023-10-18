# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(101):
    b = a + [i]
    b.sort()
    s = sum(b[1:n-1])

    if s >= x:
        print(i)
        exit()
else:
    print(-1)
