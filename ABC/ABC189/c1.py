n = int(input())
a = list(map(int, input().split()))
# n = 10**4
# a = [i+1 for i in range(n)]

res = 0
for i in range(n):
    tmp = 0
    for j in range(i+1, n):
        if a[i] <= a[j]:
            tmp += a[i]
        else:
            break
    for j in range(i, -1, -1):
        if a[i] <= a[j]:
            tmp += a[i]
        else:
            break
    res = max(res, tmp)

print(res)
