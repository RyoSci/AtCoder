import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

q = [0]*n
for i in range(n):
    q[p[i]-1] = i+1

print(*q)
