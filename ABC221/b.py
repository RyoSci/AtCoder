import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s = list(input().strip())
t = list(input().strip())

ans = "No"
if s == t:
    ans = "Yes"
else:
    n = len(s)
    s_ = s[::]
    for i in range(n-1):
        s[i], s[i+1] = s[i+1], s[i]
        if s == t:
            ans = "Yes"
        s = s_[::]

print(ans)
