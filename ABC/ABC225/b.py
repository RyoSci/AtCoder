import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
g = [0]*n

for i in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    g[a] += 1
    g[b] += 1

if n-1 in g:
    print("Yes")
else:
    print("No")
