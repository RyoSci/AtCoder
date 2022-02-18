import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

x, y = map(int, input().split())
print((max(0, y-x)+10-1)//10)
