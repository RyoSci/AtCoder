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
        res += a[i]//2
        if a[i+1] > 0:
            res += 1
            a[i+1] -= 1
        i += 1

print(res)
