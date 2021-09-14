import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

x = list(map(int, input().split()))

if 0 <= x[0] <= 400:
    ans = "Yes"
else:
    ans = "No"

for i in range(7):
    if 0 <= x[i+1]-x[i] <= 400:
        continue
    else:
        ans = "No"

print(ans)
