n = int(input())
a = list(map(int, input().split()))
res = 0
for i in range(n):
    tmp = a[i]
    while True:
        if tmp % 2 == 1 and tmp % 3 != 2:
            res += a[i] - tmp
            break
        else:
            tmp -= 1

print(res)
