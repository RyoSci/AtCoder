import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        dis = (xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2
        ans = max(ans, dis)

print(ans**0.5)
