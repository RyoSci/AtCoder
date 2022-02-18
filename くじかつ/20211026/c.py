import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

x, y = map(int, input().split())

res = 0
if x*y == 0:
    if x == 0:
        if y >= 0:
            res += y
        else:
            res += abs(y)+1
    else:
        if x > 0:
            res += x+1
        else:
            res += abs(x)
elif x*y > 0:
    if x <= y:
        res += y-x
    else:
        res += 2+x-y
else:
    if x >= 0:
        if abs(x) <= abs(y):
            res += abs(y)-abs(x)+1
        else:
            res += abs(x)-abs(y)+1
    else:
        if abs(x) <= abs(y):
            res += abs(y)-abs(x)+1
        else:
            res += abs(x)-abs(y)+1

print(res)
