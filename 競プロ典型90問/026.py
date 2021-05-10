from queue import Queue

n = int(input())
ver_edges = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    ver_edges[a].append(b)
    ver_edges[b].append(a)


color_map = [-1]*n
color_map[0] = 0
q = Queue()
q.put([0, 0])
while not q.empty():
    ver, color = q.get()
    children = ver_edges[ver]
    for chi in children:
        if color_map[chi] == -1:
            color_map[chi] = color ^ 1
            q.put([chi, color ^ 1])

ans = []
if color_map.count(0) >= n//2:
    for i in range(n):
        if color_map[i] == 0:
            ans.append(i+1)
else:
    for i in range(n):
        if color_map[i] == 1:
            ans.append(i+1)

print(*ans[:n//2])
