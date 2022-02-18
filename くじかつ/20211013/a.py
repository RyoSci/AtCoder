import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a, b = map(int, input().split())
print((a-b)/3+b)
