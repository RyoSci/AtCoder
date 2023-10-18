# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
a = list(map(int, input().split()))

b = list(range(1, n+1))


rev_pos = list(range(1, n+1))
for i in range(m-1, -1, -1):
    l, r = a[i]-1, a[i]
    rev_pos[l], rev_pos[r] = rev_pos[r], rev_pos[l]

now = 0
ans = []
for i in range(m):
    l, r = a[i]-1, a[i]
    rev_pos[l], rev_pos[r] = rev_pos[r], rev_pos[l]

    ans.append(rev_pos[now])

    if a[i] == now+1:
        now += 1
    elif a[i] == now:
        now -= 1

print(*ans)
