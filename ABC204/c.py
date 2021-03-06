from queue import Queue
n, m = map(int, input().split())

roads = [[] for i in range(n)]
# roads = [[i, (i+1) % n] for i in range(n)]

for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    roads[a].append(b)

res = 0
for i in range(n):
    # q = Queue()
    # q.put(i)
    q = [i]
    tmp = set()
    tmp.add(i)
    for pare in q:
        children = roads[pare]
        for chi in children:
            if chi not in tmp:
                tmp.add(chi)
                # q.put(chi)
                q.append(chi)
    res += len(tmp)

print(res)
