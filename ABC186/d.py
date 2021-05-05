n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

rest = sum(a)

ans = 0
for i in range(n-1):
    rest -= a[i]
    ans += a[i]*(n-1-i) - rest

print(ans)
