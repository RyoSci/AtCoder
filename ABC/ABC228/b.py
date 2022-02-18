import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))

s = set()
for i in range(2*n):
    if x in s:
        break
    s.add(x)
    x = a[x-1]

print(len(s))
