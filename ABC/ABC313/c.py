# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
a.sort()

asum = sum(a)
x = asum//n
b = [x]*n
for i in range(asum % n):
    b[n-i-1] += 1

# print(b)

ans = 0
for i in range(n):
    if a[i] < b[i]:
        ans += b[i]-a[i]

print(ans)
