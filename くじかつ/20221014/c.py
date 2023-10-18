# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, x = map(int, input().split())

l = []
a = []
for i in range(n):
    li, *ai = list(map(int, input().split()))
    l.append(li)
    a.append(ai)


def f(i, res):
    if res > x:
        return 0
    if i == n:
        if res == x:
            return 1
        else:
            return 0
    ans = 0
    for k in a[i]:
        ans += f(i+1, res*k)
    return ans


ans = f(0, 1)
print(ans)
