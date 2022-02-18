from queue import Queue
n = int(input())
ver_edge_len = [[] for i in range(n)]

for i in range(n - 1):
    u, v, w = map(int, input().split())
    ver_edge_len[u - 1].append([v, w])
    ver_edge_len[v - 1].append([u, w])

ver_colors = [-1] * n
ver_colors[0] = 0

q = Queue()

for i in ver_edge_len[0]:
    q.put([1, i])

while not q.empty():
    pair, [chi, w] = q.get()
    ver_colors[chi - 1] = ver_colors[pair - 1] ^ (w % 2)
    for grand_chi in ver_edge_len[chi - 1]:
        if ver_colors[grand_chi[0] - 1] == -1:
            q.put([chi, grand_chi])


for i in range(n):
    print(ver_colors[i])
