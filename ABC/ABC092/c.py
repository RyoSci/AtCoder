n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [0]

max_fee = 0
for i in range(1, n + 2):
    max_fee += abs(a[i] - a[i - 1])

for i in range(1, n + 1):
    if a[i - 1] <= a[i] <= a[i + 1] or a[i + 1] <= a[i] <= a[i - 1]:
        print(max_fee)
    else:
        res = max_fee + a[i + 1] - a[i] + a[i] - a[i - 1]
        print(res)
