# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

d = dict()

pe = []

for i in range(n):
    m = int(input())
    tmp = []
    for j in range(m):
        p, e = map(int, input().split())
        tmp.append((p, e))
        if (p, e) not in d:
            d[(p, e)] = 0
        d[(p, e)] += 1
    pe.append(tmp)

# print(d)
p_es = dict()
for key, val in d.items():
    p, e = key
    if p not in p_es:
        p_es[p] = [0]
    p_es[p].append(e)

ans = set()

tot = []
for key in p_es.keys():
    p_es[key].sort()
    tot.append(p_es[key][-1])

# print(p_es)

# print(pe)

for i in range(n):
    tmp = []
    for p, e in pe[i]:
        index = bisect_left(p_es[p], e)
        if index == len(p_es[p])-1:
            if d[(p, e)] > 1:
                # tmp.append((p, e))
                continue
            else:
                tmp.append((p, p_es[p][index-1]))
        else:
            # tmp.append((p, p_es[p][-1]))
            continue
    tmp.sort()
    ans.add(tuple(tmp))

print(len(ans))
# print(ans)
