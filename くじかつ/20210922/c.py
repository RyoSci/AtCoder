from bisect import bisect_left
from abc import abstractproperty
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


h, w, n = map(int, input().split())
x = set()
y = set()

query = []

for i in range(n):
    a, b = map(int, input().split())
    x.add(a)
    y.add(b)
    query.append([a, b])

x = list(x)
x.sort()
y = list(y)
y.sort()

ans = []
for a, b in query:
    ai = bisect_left(x, a)
    bi = bisect_left(y, b)
    ans.append([ai+1, bi+1])


for i in range(n):
    print(*ans[i])
