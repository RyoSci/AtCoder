n = int(input())
a = list(map(int, input().split()))
res = 10**18

total = sum(a)
cnt = 0
for i in range(n):
    cnt += a[i]
    tmp = abs(total-cnt-cnt)
    res = min(res, tmp)

print(res)
