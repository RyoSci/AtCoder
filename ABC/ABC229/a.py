import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

ans = "No"
if s1[0] == "#" and s1[1] == "#":
    ans = "Yes"
if s2[0] == "#" and s2[1] == "#":
    ans = "Yes"
if s1[0] == "#" and s2[0] == "#":
    ans = "Yes"
if s1[1] == "#" and s2[1] == "#":
    ans = "Yes"

print(ans)
