# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, x = map(int, input().split())
s = input().strip()

# n = 10**6
# x = 10**18
# s = "R"*(n//2)
# s += "U"*(n//2)

d = deque()

u = 0
for i in range(n):
    if s[i] == "L":
        d.append(s[i])
    elif s[i] == "R":
        d.append(s[i])
    else:
        if len(d) > 0 and d[-1] != "U":
            d.pop()
        else:
            d.append(s[i])

while len(d) > 0:
    now = d.popleft()
    if now == "L":
        x *= 2
    elif now == "R":
        x *= 2
        x += 1
    else:
        x //= 2

print(x)
