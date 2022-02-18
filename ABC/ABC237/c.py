import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s = input().strip()
n = len(s)

if s == s[::-1]:
    print("Yes")
    exit()

l = 0
for i in range(n):
    if s[i] == "a":
        l += 1
    else:
        break

r = 0
for i in range(n-1, -1, -1):
    if s[i] == "a":
        r += 1
    else:
        break

if s[l:n-r] == s[l:n-r][::-1] and l <= r:
    print("Yes")
else:
    print("No")
