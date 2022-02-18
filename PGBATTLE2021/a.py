import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

x, y, k = map(int, input().split())
print(y-k/x)
