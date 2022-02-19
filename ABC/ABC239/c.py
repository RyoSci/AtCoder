import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

x1,y1,x2,y2 = list(map(int, input().split()))

ans="No"
for dx, dy in [[2,1],[1,2],[-1,2],[-2,1], [-2,-1],[-1,-2],[1,-2],[2,-1]]:
    nx=x1+dx
    ny=y1+dy
    if (nx-x2)**2+(ny-y2)**2==5:
        ans="Yes"
        break

print(ans)