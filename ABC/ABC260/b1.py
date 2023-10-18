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


def f(xyz, meme):
    for i in range(n):
        if xyz == 0:
            break
        _, j = meme[i]
        if seen[j] == 0:
            seen[j] = 1
            ans.append(j+1)
            xyz -= 1
    return


f(x, m)
f(y, e)
f(z, me)

ans.sort()
print(*ans)
