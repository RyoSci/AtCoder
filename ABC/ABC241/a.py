import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a = list(map(int, input().split()))
now=0
for i in range(3):
    now=a[now]

print(now)