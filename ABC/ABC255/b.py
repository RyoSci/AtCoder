# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
a = list(map(lambda x: int(x)-1, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]

b = []
for i in range(n):
    if i not in a:
        b.append(i)

ans = 0
for bi in b:
    dis = INF
    for ai in a:
        tmp = 0
        tmp += (xy[ai][0]-xy[bi][0])**2
        tmp += (xy[ai][1]-xy[bi][1])**2
        tmp = tmp**(0.5)
        dis = min(dis, tmp)
    ans = max(ans, dis)

print(ans)
