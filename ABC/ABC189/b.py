n, x = map(int, input().split())
res = 0
for i in range(n):
    v, p = map(int, input().split())
    res += v*p
    if res > x*100:
        ans = i+1
        break
else:
    ans = -1

print(ans)
