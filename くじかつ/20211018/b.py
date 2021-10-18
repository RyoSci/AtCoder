import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s = input().strip()
t = ""
for i in s:
    if i == "C" or i == "F":
        t += i

if "CF" in t:
    print("Yes")
else:
    print("No")
