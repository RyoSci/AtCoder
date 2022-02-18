m, n, N = map(int, input().split())

ans = 0
new = N
old = 0
while new != 0:
    ans += new
    old += new
    new = old // m * n
    old = old % m

print(ans)
