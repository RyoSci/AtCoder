import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

x = int(input())
a = int(input())
b = int(input())

res = max(0, x-a) % b
print(res)
