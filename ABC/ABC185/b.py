n, m, t = map(int, input().split())
n_ = n
now = 0
ans = "Yes"
for i in range(m):
    a, b = map(int, input().split())
    n -= a-now
    if n <= 0:
        ans = "No"
        break
    n += b-a
    n = min(n_, n)
    now = b
n -= t-now
if n <= 0:
    ans = "No"

print(ans)
