# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = []
for i in range(n):
    c.append((a[i], 0))

for i in range(m):
    c.append((b[i], 1))

c.sort()

a = []
b = []
for i in range(n+m):
    if c[i][1] == 0:
        a.append(i+1)
    else:
        b.append(i+1)

print(*a)
print(*b)
