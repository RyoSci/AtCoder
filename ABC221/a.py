import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a, b = map(int, input().split())
print(32**(a-b))
