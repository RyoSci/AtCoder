import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m, d = map(int, input().split())

res = 0
for i in range(1, m+1):
    for j in range(1, d+1):
        if (j//10)*(j % 10) == i and j//10 >= 2 and j % 10 >= 2:
            res += 1

print(res)
