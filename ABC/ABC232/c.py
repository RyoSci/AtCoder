from itertools import permutations
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
gt = [[0]*n for _ in range(n)]
ga = [[0]*n for _ in range(n)]

for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    gt[a][b] = 1
    gt[b][a] = 1

for i in range(m):
    c, d = map(lambda x: int(x)-1, input().split())
    ga[c][d] = 1
    ga[d][c] = 1

ans = False
for i in permutations(range(n)):
    tmp = True
    for j in range(n-1):
        for k in range(j+1, n):
            nj = i[j]
            nk = i[k]
            if gt[j][k] != ga[nj][nk]:
                tmp = False
                break
    if tmp:
        ans = True
if ans:
    print("Yes")
else:
    print("No")
