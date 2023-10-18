# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = []
for i in range(n):
    ai = list(input())
    a.append(ai)

d = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1)
]


ans = 0
for i in range(n):
    for j in range(n):
        for dx, dy in d:
            res = a[i][j]
            for k in range(1, n):
                ni = i+dx*k
                ni %= n
                nj = j+dy*k
                nj %= n
                res += a[ni][nj]
            ans = max(ans, int(res))

print(ans)
