import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

edge_list = [[] for i in range(n)]
for i in range(m):
    c, d = map(lambda x: int(x) - 1, input().split())
    edge_list[c].append(d)
    edge_list[d].append(c)


def dfs(pair):
    global group_sum_a, group_sum_b
    childlen = edge_list[pair]
    for chi in childlen:
        if already_groped[chi] == 0:
            group_sum_a += a[chi]
            group_sum_b += b[chi]
            already_groped[chi] = 1
            dfs(chi)
    return


ans = "Yes"
if m == 0 and a[0] != b[0]:
    ans = "No"

already_groped = [0] * n
for i in range(n):
    if already_groped[i]:
        continue
    group_sum_a = 0
    group_sum_b = 0
    dfs(i)
    if group_sum_a != group_sum_b:
        ans = "No"
        break
print(ans)
