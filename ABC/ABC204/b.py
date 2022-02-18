n = int(input())
a = list(map(int, input().split()))
res = 0
for i in range(n):
    if a[i] > 10:
        res += a[i]-10
print(res)
