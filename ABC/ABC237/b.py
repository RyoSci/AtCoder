import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

a = list(zip(*a))

for i in range(w):
    print(*a[i])
