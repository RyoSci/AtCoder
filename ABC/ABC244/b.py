# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = 10**18

n = int(input())
t = input().strip()

x = 0
y = 0
direction = 0

for i in range(n):
    if t[i] == "S":
        if direction == 0:
            x += 1
        elif direction == 1:
            y -= 1
        elif direction == 2:
            x -= 1
        else:
            y += 1
    else:
        direction += 1
        direction %= 4

print(x, y)
