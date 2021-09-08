import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s, t = input().split()

if s < t:
    print("Yes")
else:
    print("No")
