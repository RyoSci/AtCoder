from collections import deque
import heapq
from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


a = []
heapq.heapify(a)

q = int(input())
d = deque()

for i in range(q):
    n, *x = map(int, input().split())
    if n == 1:
        d.append(x[0])
    elif n == 2:
        if len(a) > 0:
            print(heapq.heappop(a))
        else:
            print(d.popleft())
    else:
        k = len(d)
        for j in range(k):
            heapq.heappush(a, d.popleft())
