# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m, d = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort(reverse=True)
b.sort(reverse=True)


i = 0
j = 0
while i < n and j < m:
    if abs(a[i]-b[j]) <= d:
        print(a[i]+b[j])
        exit()
    elif a[i] > b[j]:
        i += 1
    elif a[i] < b[j]:
        j += 1
else:
    print(-1)
