# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a))
a.sort()

ans = 0
for i in range(min(k, len(a))):
    if a[i] == ans:
        ans += 1

print(ans)
