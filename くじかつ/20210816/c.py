n = int(input())
i = 1
a = 0
res = 0
while a < n:
    if (n-a) % i == 0:
        res += 2
    a += i
    i += 1

print(res)
