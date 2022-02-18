from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
k = [0]*m
a = []
for i in range(m):
    ki = int(input())
    ai = list(map(int, input().split()))
    # k.append(ki)
    a.append(ai)

table = dict()
next = [[] for _ in range(n)]

for i in range(m):
    if a[i][0] not in table:
        table[a[i][0]] = 0
    table[a[i][0]] += 1
    k[i] += 1
    next[a[i][0]-1].append(i)

q = deque()
for key, val in table.items():
    if val == 2:
        q.append(key)

while len(q) > 0:
    key = q.popleft()
    for next_box in next[key-1]:
        if len(a[next_box]) > k[next_box]:
            if a[next_box][k[next_box]] not in table:
                table[a[next_box][k[next_box]]] = 0
            table[a[next_box][k[next_box]]] += 1
            if table[a[next_box][k[next_box]]] == 2:
                q.append(a[next_box][k[next_box]])
            next[a[next_box][k[next_box]]-1].append(next_box)
            k[next_box] += 1
    del table[key]


if len(table) == 0:
    print("Yes")
else:
    print("No")
