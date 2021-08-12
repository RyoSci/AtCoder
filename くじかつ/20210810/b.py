n = int(input())
a = list(map(int, input().split()))

sum_a = sum(a)

ans = -1
tmp = 10**6
for i in range(n):
    if abs(sum_a-a[i]*n) < abs(sum_a-tmp*n):
        tmp = a[i]
        ans = i

print(ans)
