# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
# n = 1000
# a = [2**20*3**10 for i in range(n)]

d = dict()

for i in range(n):
    ai = a[i]
    cnt = 0
    q = []
    q.append([ai, cnt])
    tmp_d = dict()
    while len(q) > 0:
        ai, cnt = q.pop()
        if ai not in tmp_d:
            tmp_d[ai] = cnt
        else:
            # tmp_d[ai] = min(tmp_d[ai], cnt)
            continue

        if ai % 2 == 0:
            q.append([ai//2, cnt+1])
        if ai % 3 == 0:
            q.append([ai//3, cnt+1])

    for key, val in tmp_d.items():
        if key not in d:
            d[key] = []
        d[key].append(val)


ans = INF
for key, vals in d.items():
    if len(vals) == n:
        ans = min(ans, sum(vals))

if ans == INF:
    print(-1)
else:
    print(ans)
