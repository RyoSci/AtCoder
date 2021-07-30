n = int(input())
a = [0]*(n+1)

for i in range(n):
    ai = int(input())
    a[i+1] += ai

res = 0
i = 0
while i <= n:
    if i == n:
        res += a[i]//2
        i += 1
        break
    if a[i] % 2 == 0:
        res += a[i]//2
        i += 1
    else:
        if a[i] == a[i+1]:
            res += a[i]
            i += 2
        else:
            res += a[i]//2
            i += 1

print(res)
