import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
res = 10**18
for p in range(1, 101):
    tmp = 0
    for i in range(n):
        tmp += (x[i]-p)**2
    res = min(res, tmp)

print(res)
