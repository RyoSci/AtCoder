import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s, w = map(int, input().split())
if s > w:
    print("safe")
else:
    print("unsafe")
