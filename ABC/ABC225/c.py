import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]

ans = "Yes"
for i in range(n):
    for j in range(m-1):
        l = b[i][j] % 7
        r = b[i][j+1] % 7
        if l == 0:
            l = 7
        if r == 0:
            r = 7
        if l+1 == r:
            continue
        else:
            ans = "No"
            print(ans)
            exit()

for j in range(m):
    for i in range(n-1):
        l = b[i][j]
        r = b[i+1][j]
        if l+7 == r:
            continue
        else:
            ans = "No"
            print(ans)
            exit()

print(ans)
