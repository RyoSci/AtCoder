import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

w, k, d = map(int, input().split())

if d >= k and d >= (w-k):
    print("Yes")
else:
    print("No")
