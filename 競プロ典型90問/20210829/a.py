import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]

cnt = 0
for x in range(h-1):
    for y in range(w-1):
        dis = a[x][y]-b[x][y]
        if dis == 0:
            continue
        cnt += abs(dis)
        for dx, dy in zip([0, 0, 1, 1], [0, 1, 0, 1]):
            nx = x+dx
            ny = y+dy
            a[nx][ny] -= dis

if a == b:
    print("Yes", cnt, sep="\n")
else:
    print("No")
