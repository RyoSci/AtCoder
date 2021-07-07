n = int(input())
a = list(map(int, input().split()))
# n = 10**4
# a = [i+1 for i in range(n)]

res = 0
for l in range(n):
    flag = a[l]
    for r in range(l, n):
        if flag > a[r]:
            flag = a[r]
        res = max(res, flag*(r-l+1))

print(res)
