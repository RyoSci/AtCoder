import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
s = set()
for i in range(n):
    l, *a = list(map(int, input().split()))
    a = tuple(a)
    s.add(a)
print(len(s))
