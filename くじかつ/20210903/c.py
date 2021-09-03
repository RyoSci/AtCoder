import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
a = [1]*(n+1)

for i in range(1, n):
    for j in range(2*i, n+1, i):
        if a[i] == a[j]:
            a[j] = a[i]+1

print(*a[1:])
