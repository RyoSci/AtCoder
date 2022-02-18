import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s = input().strip()
AtCoder = "AtCoder"

if s == AtCoder:
    ans = "Yes"
elif s.lower() == AtCoder.lower():
    ans = "Maybe"
else:
    ans = "No"

print(ans)
