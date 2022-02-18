from queue import Queue

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

edge_list = [[] for i in range(n)]
for i in range(m):
    c, d = map(lambda x: int(x) - 1, input().split())
    edge_list[c].append(d)
    edge_list[d].append(c)


def bfs(pair):
    global group_sum_a, group_sum_b
    already_grouped[pair] = 1
    group_sum_a += a[pair]
    group_sum_b += b[pair]

    q = Queue()
    q.put(edge_list[pair])
    while not q.empty():
        childrlen = q.get()
        for chi in childrlen:
            if already_grouped[chi] == 0:
                group_sum_a += a[chi]
                group_sum_b += b[chi]
                already_grouped[chi] = 1
                q.put(edge_list[chi])
    return


ans = "Yes"
if m == 0 and a[0] != b[0]:
    ans = "No"

already_grouped = [0] * n
for i in range(n):
    if already_grouped[i]:
        continue
    group_sum_a = 0
    group_sum_b = 0
    bfs(i)
    if group_sum_a != group_sum_b:
        ans = "No"
        break
print(ans)
