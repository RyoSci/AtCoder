from queue import Queue

n, m = map(int, input().split())
roads = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    roads[a].append(b)
    roads[b].append(a)

groups = [-1] * n

for i in range(n):
    if groups[i] != -1:
        continue
    groups[i] = i
    q = Queue()
    q.put(i)
    while not q.empty():
        pair = q.get()
        children = roads[pair]
        for chi in children:
            if groups[chi] != -1:
                continue
            groups[chi] = i
            q.put(chi)

print(len(set(groups)) - 1)
