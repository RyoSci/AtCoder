# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m, k = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1

for i in range(k):
    a, b = map(int, input().split())

p = [5000]*n
b = [1]*m

print(*p)
print(*b)
