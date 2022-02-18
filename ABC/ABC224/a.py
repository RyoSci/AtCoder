import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s = input().strip()

if s[-2:] == "er":
    print("er")
else:
    print("ist")
