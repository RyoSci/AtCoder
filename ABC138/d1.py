import sys
from queue import Queue
n, q = map(int, input().split())
par2chi = [[] for i in range(n)]
counter = [0] * n

for i in range(n - 1):
    a, b = map(int, input().split())
    par2chi[a - 1].append(b - 1)
    par2chi[b - 1].append(a - 1)

for i in range(q):
    p, x = map(int, input().split())
    counter[p - 1] += x

memo = set()

sys.setrecursionlimit(10 ** 6)


def dfs(par):
    children = par2chi[par]
    memo.add(par)
    for child in children:
        if child in memo:
            continue
        counter[child] += counter[par]
        dfs(child)


dfs(0)

print(*counter)
# print(par2chi)
