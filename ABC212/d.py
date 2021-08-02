import heapq
a = []
heapq.heapify(a)

q = int(input())
now = 0
for i in range(q):
    p, *x = map(int, input().split())
    if p != 3:
        x = x[0]
    if p == 1:
        heapq.heappush(a, x-now)
    elif p == 2:
        now += x
    else:
        tmp = heapq.heappop(a)
        print(tmp+now)
