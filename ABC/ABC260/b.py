# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, x, y, z = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = []
e = []
me = []
for i in range(n):
    m.append([-a[i], i])
    e.append([-b[i], i])
    me.append([-(a[i]+b[i]), i])

m.sort()
e.sort()
me.sort()

seen = [0]*n

ans = []
now = 0
while x > 0:
    _, i = m[now]
    if seen[i] == 0:
        seen[i] = 1
        ans.append(i+1)
        x -= 1
    now += 1

now = 0
while y > 0:
    _, i = e[now]
    if seen[i] == 0:
        seen[i] = 1
        ans.append(i+1)
        y -= 1
    now += 1

now = 0
while z > 0:
    _, i = me[now]
    if seen[i] == 0:
        seen[i] = 1
        ans.append(i+1)
        z -= 1
    now += 1

ans.sort()
print(*ans)
