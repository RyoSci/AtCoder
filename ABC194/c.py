n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)
sum_a_2 = 0
for i in range(n):
    sum_a_2 += a[i] ** 2

res = 0
for i in range(n):
    sum_a_2 -= a[i] ** 2
    sum_a -= a[i]
    res += sum_a_2
    res += (n - i - 1) * a[i] ** 2
    res += -2 * a[i] * sum_a

print(res)
