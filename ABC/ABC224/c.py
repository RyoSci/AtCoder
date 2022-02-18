import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            x3, y3 = xy[k]
            if (x3-x1)*(y2-y1) == (x2-x1)*(y3-y1):
                continue
            else:
                res += 1

print(res)
