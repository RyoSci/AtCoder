import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

h, w = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(h)]

for i in range(h-1):
    for ii in range(i+1, h):
        for j in range(w-1):
            for jj in range(j+1, w):
                if a[i][j]+a[ii][jj] <= a[ii][j]+a[i][jj]:
                    continue
                else:
                    print("No")
                    exit()
else:
    print("Yes")
