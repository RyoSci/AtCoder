import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

x = int(input())
if x > 0 and x % 100 == 0:
    print("Yes")
else:
    print("No")
