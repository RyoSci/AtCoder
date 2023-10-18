# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

ans = []

for i in range(n-1):
    if abs(a[i]-a[i+1]) <= 1:
        ans.append(a[i])
    else:
        if a[i] > a[i+1]:
            pm = -1
        else:
            pm = 1

        for j in range(a[i], a[i+1], pm):
            ans.append(j)

ans.append(a[n-1])
print(*ans)
