"""
優先度付きキューで実装
"""
import heapq

n, m = map(int, input().split())
a_list = list(map(int, input().split()))

a_pq = []

for i in a_list:
    heapq.heappush(a_pq, [-i, 1])

for i in range(m):
    b, c = map(int, input().split())
    heapq.heappush(a_pq, [-c, b])

ans = 0
for i in range(n):
    pop_tmp = heapq.heappop(a_pq)
    number, sum_number = pop_tmp
    ans += -number
    if sum_number > 1:
        sum_number -= 1
        heapq.heappush(a_pq, [number, sum_number])

print(ans)
