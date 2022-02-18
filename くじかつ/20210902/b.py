import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a, b = map(int, input().split())
s = input()
num = "0123456789"

ans = "Yes"
for i in range(a+b+1):
    if i == a:
        if s[i] == "-":
            continue
        else:
            ans = "No"
    else:
        if s[i] in num:
            continue
        else:
            ans = "No"

print(ans)
