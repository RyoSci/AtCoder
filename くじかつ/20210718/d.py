from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    g[a].append(b)
    g[b].append(a)

res = 0
for i in range(n):
    for j in g[i]:
        q = deque()
        q.append(0)
        memo = [0]*n
        memo[0] = 1
        while len(q) != 0:
            pair = q.popleft()
            for chi in g[pair]:
                if pair == i and chi == j or pair == j and chi == i:
                    continue
                if memo[chi] == 0:
                    memo[chi] = 1
                    q.append(chi)
        if sum(memo) != n:
            res += 1

print(res//2)
