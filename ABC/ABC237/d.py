from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n = int(input())
s = input().strip()

dq = deque()
dq.append(n)

for i in range(n-1, -1, -1):
    if s[i] == "L":
        dq.append(i)
    else:
        dq.appendleft(i)

print(*dq)
