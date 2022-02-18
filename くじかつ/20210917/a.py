import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, i = map(int, input().split())
print(n-i+1)
