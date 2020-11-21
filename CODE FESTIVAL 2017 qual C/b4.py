n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(3 ** n):
    res = 1
    for j in range(n):
        mod = i % 3
        i = i // 3
        res = (res * (a[j] + mod - 1)) % 2
        if res % 2 == 0:
            break
    if res % 2 == 0:
        ans += 1

print(ans)
