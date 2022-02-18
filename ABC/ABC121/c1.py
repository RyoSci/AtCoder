import heapq
n, m = map(int, input().split())
a_b = []

for i in range(n):
    ab = list(map(int, input().split()))
    a_b.append(ab)

heapq.heapify(a_b)

res = 0
for i in range(m):
    tmp_a, tmp_b = heapq.heappop(a_b)
    res += tmp_a 
    tmp_b -= 1
    if tmp_b > 0:
        heapq.heappush(a_b, [tmp_a, tmp_b])

print(res)