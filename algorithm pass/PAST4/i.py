n = int(input())
a = list(map(int, input().split()))
l = 0
r = 0
sum_a = sum(a)
tmp = a[0]
res = 10 ** 18
while True:
    res = min(res, abs(sum_a - 2 * tmp))
    if 2 * tmp >= sum_a:
        break
    else:
        r += 1
        tmp += a[r]

while r != -1:
    if 2 * tmp >= sum_a:
        tmp -= a[r]
        r -= 1
    else:
        l -= 1
        tmp += a[l]
    res = min(res, abs(sum_a - 2 * tmp))

print(res)
