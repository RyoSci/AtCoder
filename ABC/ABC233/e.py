import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

x = [int(i) for i in input().strip()]
# x = [1]*(2*10**5)
n = len(x)
now = sum(x)
ans = [""] * (n+10)
rest = 0
for i in range(n):
    ans[n+10-i-1] = str((now+rest) % 10)
    rest = (now+rest)//10
    now -= x[n-i-1]
    # print(now, rest, ans)
if rest > 0:
    ans[n+10-n-1] = str(rest)
print("".join(ans))
