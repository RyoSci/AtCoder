n, d = map(int, input().split())
ans = 0
for i in range(n):
    x, y = map(int, input().split())
    tmp_d = x ** 2 + y ** 2
    if tmp_d <= d ** 2:
        ans += 1
print(ans)