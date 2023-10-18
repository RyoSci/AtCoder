# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())

ans = 0
a = []
for i in range(m):
    c = int(input())
    ai = list(map(lambda x: int(x)-1, input().split()))
    a.append(ai)

for i in range(1 << m):
    mask = 0

    for j in range(m):
        if i >> j & 1:
            for k in a[j]:
                mask |= (1 << k)

    if mask == (1 << n)-1:
        ans += 1

print(ans)
