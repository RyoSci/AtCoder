import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s = input().strip()
t = input().strip()

n = len(s)

ans = True
for i in range(n-1):
    if (ord(s[i])-ord(s[i+1])) % 26 != (ord(t[i])-ord(t[i+1])) % 26:
        ans = False

if ans:
    print("Yes")
else:
    print("No")
