import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s = input().strip()
t = "oxx"*10**5

if s in t:
    print("Yes")
else:
    print("No")
