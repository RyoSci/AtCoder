# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

p_e_cnt = dict()

pe = []

for i in range(n):
    m = int(input())
    tmp = []
    for j in range(m):
        p, e = map(int, input().split())
        tmp.append((p, e))
        if (p, e) not in p_e_cnt:
            p_e_cnt[(p, e)] = 0
        p_e_cnt[(p, e)] += 1
    pe.append(tmp)

# print(p_e_cnt)
p_dict_es_list = dict()
for key, val in p_e_cnt.items():
    p, e = key
    if p not in p_dict_es_list:
        p_dict_es_list[p] = [0]
    p_dict_es_list[p].append(e)

ans = set()

for key in p_dict_es_list.keys():
    p_dict_es_list[key].sort()

# print(p_dict_es_list)

# print(pe)

for i in range(n):
    tmp = []
    for p, e in pe[i]:
        index = bisect_left(p_dict_es_list[p], e)
        if index == len(p_dict_es_list[p])-1:
            if p_e_cnt[(p, e)] > 1:
                # tmp.append((p, e))
                continue
            else:
                tmp.append((p, p_dict_es_list[p][index-1]))
        else:
            # tmp.append((p, p_dict_es_list[p][-1]))
            continue
    tmp.sort()
    ans.add(tuple(tmp))

print(len(ans))
# print(ans)
