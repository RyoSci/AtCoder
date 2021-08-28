import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
c = [[0]*(n+1) for _ in range(2)]

for i in range(n):
    ci, pi = map(int, input().split())
    c[ci-1][i+1] = pi

for i in range(2):
    for j in range(n):
        c[i][j+1] += c[i][j]

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(c[0][r]-c[0][l-1], c[1][r]-c[1][l-1])
