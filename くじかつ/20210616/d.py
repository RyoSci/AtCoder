import heapq as hq

n, m = map(int, input().split())
a = list(map(lambda x: -int(x), input().split()))

hq.heapify(a)

for i in range(m):
    tmp = hq.heappop(a)
    hq.heappush(a, int(tmp/2))
print(-sum(a))
