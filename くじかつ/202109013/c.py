import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

w, h, n = map(int, input().split())
min_x = 0
max_x = w
min_y = 0
max_y = h

for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        min_x = max(min_x, x)
    elif a == 2:
        max_x = min(max_x, x)
    elif a == 3:
        min_y = max(min_y, y)
    elif a == 4:
        max_y = min(max_y, y)


print(max(0, max_x-min_x)*max(0, max_y-min_y))
