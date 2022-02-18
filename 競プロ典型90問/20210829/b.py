from itertools import permutations
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

m = int(input())

relations = [[0]*n for _ in range(n)]
for i in range(m):
    x, y = map(lambda x: int(x)-1, input().split())
    relations[x][y] = 1
    relations[y][x] = 1

res = 10**18
for p in permutations(range(n)):
    cnt = 0
    i = -1
    for i in range(n-1):
        if relations[p[i]][p[i+1]] == 1:
            break
        cnt += a[p[i]][i]
    else:
        i += 1
        cnt += a[p[i]][i]
        res = min(res, cnt)

if res == 10**18:
    print(-1)
else:
    print(res)
