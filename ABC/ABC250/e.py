# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18
MOD = 10**9+7

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
q = int(input())
xy = [list(map(int, input().split())) for _ in range(q)]

a_add = [0]*(n+1)
a_mul = [1]*(n+1)
a_set = set()
for i in range(n):
    if a[i] in a_set:
        a_add[i+1] = a_add[i]
        a_mul[i+1] = a_mul[i]
    else:
        a_set.add(a[i])
        a_add[i+1] = a_add[i]+a[i]
        a_mul[i+1] = a_mul[i]*a[i]
        a_mul[i+1] %= MOD

b_add = [0]*(n+1)
b_mul = [1]*(n+1)
b_set = set()
for i in range(n):
    if b[i] in b_set:
        b_add[i+1] = b_add[i]
        b_mul[i+1] = b_mul[i]
    else:
        b_set.add(b[i])
        b_add[i+1] = b_add[i]+b[i]
        b_mul[i+1] = b_mul[i]*b[i]
        b_mul[i+1] %= MOD

ans = []
for i in range(q):
    x, y = xy[i]
    if a_add[x] == b_add[y] and a_mul[x] == b_mul[y]:
        ans.append("Yes")
    else:
        ans.append("No")

print(*ans, sep="\n")
