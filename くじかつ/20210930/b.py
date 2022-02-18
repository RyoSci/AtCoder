import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

integers = set()
for i in range(1, 200):
    integers.add(i**2)


n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(n-1):
    for j in range(i+1, n):
        dis = 0
        for k in range(d):
            dis += (x[i][k]-x[j][k])**2
        if dis in integers:
            res += 1
print(res)
