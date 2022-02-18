n = int(input())
a = list(map(int, input().split()))

# n = 10**4
# a = [i for i in range(n)]

res = 0
for i in range(n):
    tmp = a[i]
    for j in range(i, n):
        tmp = min(tmp, a[j])
        res = max(res, tmp*(j-i+1))

print(res)
