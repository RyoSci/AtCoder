# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m, t = map(int, input().split())
a = [0] + list(map(int, input().split()))
x = []
y = []
for i in range(m):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)


bonus = [0]*(n+1)
for i in range(m):
    bonus[x[i]] = y[i]

now = 1
while t > 0 and now < n:
    t += bonus[now]
    t -= a[now]
    now += 1

if now == n and t > 0:
    print("Yes")
else:
    print("No")
