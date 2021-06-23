n = int(input())
a = list(map(int, input().split()))
res = 1000

for i in range(1, n):
    res = max(res, res//a[i-1]*a[i]+res % a[i-1])

print(res)
