# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import heapq
import sys
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m, k = map(int, input().split())
abc = []
for i in range(m):
    a, b, c = map(int, input().split())
    abc.append([a-1, b-1, c])

e = list(map(int, input().split()))

nexts = [[] for _ in range(n)]
for i in range(k):
    a, b, c = abc[e[i]-1]
    nexts[a].append([b, i])

dis = [INF]*n
dis[0] = 0


q = []
heapq.heapify(q)

heapq.heappush(q, [0, 0, -1])

while len(q) > 0:
    c, node, indexi = heapq.heappop(q)
    if dis[node] < c:
        continue
    for next, indexj in nexts[node]:
        if indexj > indexi and dis[next] > c+abc[e[indexj]-1][-1]:
            dis[next] = c+abc[e[indexj]-1][-1]
            heapq.heappush(
                q, [c+abc[e[indexj]-1][-1], next, indexj])


if dis[n-1] == INF:
    print(-1)
else:
    print(dis[n-1])
