# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left, bisect_right
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, q, x = list(map(int, input().split()))
w = list(map(int, input().split()))
w_tot = [0]*(n+1)
for i in range(n):
    w_tot[i+1] = w_tot[i]+w[i]
w_tot.append(INF)

p = []
# bef_cycle = [0]*n
# aft_cycle = [0]*n
seen = [-1]*n
box_w = 0
box_n = 0
now = 0
for i in range(n+10):
    if seen[now] != -1:
        # サイクル検出
        bef_cycle = p[0:seen[now]]
        aft_cycle = p[seen[now]:]
        break
    seen[now] = i
    tmp = x+w_tot[now]
    pos = bisect_left(w_tot, tmp)
    if w_tot[pos] == INF:
        box_n += n-now
        box_w += w_tot[-2]-w_tot[now]
        rest_w = x-(w_tot[-2]-w_tot[now])
        tmp = rest_w//w_tot[-2]
        box_n += n*tmp
        box_w += w_tot[-2]*tmp
        rest_w = rest_w % w_tot[-2]
        pos = bisect_left(w_tot, rest_w)
        box_n += pos
        # bef_cycle[now]=box_n
        p.append(box_n)
        box_n = 0
        box_w = 0
        now = pos
        now %= n
    else:
        box_n += pos-now
        # bef_cycle[now]=box_n
        p.append(box_n)
        box_n = 0
        box_w = 0
        now = pos
        now %= n


cycle_num = len(aft_cycle)

ans = []
for i in range(q):
    k = int(input())
    if k <= len(bef_cycle):
        ans.append(bef_cycle[k-1])
    else:
        k -= len(bef_cycle)
        k %= cycle_num
        ans.append(aft_cycle[k-1])

print(*ans)
