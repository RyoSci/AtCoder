n = int(input())
a = list(map(int, input().split()))
res = 0
ans = a[0]
for i in range(2, 1001):
    tmp = 0
    for j in range(n):
        if a[j] % i == 0:
            tmp += 1
    if res < tmp:
        res = tmp
        ans = i

print(ans)
