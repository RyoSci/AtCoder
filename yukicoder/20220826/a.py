# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, x, m = map(int, input().split())
a = list(map(int, input().split()))

cnts = [0]*n
for i in range(n):
    tmp = a[i]
    cnt = 0
    while tmp >= x:
        tmp //= 2
        cnt += 1
    cnts[i] = cnt


now = 0
for k in range(n, 0, -1):
    cnts[k-1] = max(0, cnts[k-1]-now)
    while cnts[k-1] > 0:
        if not (1 <= k <= min(n, m)):
            break
        now += 1
        cnts[k-1] -= 1
        m -= k

if sum(cnts) == 0:
    print("Yes")
else:
    print("No")
