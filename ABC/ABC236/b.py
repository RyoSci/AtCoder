import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

memo = [0]*n
for i in range(4*n-1):
    memo[a[i]-1] += 1

for i in range(n):
    if memo[i] < 4:
        print(i+1)
        exit()
