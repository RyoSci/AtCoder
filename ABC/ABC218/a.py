import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
s = input().strip()

if s[n-1] == "o":
    print("Yes")
else:
    print("No")
