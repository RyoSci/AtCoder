import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a, b = map(int, input().split())
print(max(0, a-2*b))
