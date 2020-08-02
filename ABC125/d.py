n = int(input())
a = list(map(int, input().split()))

minus_counter = 0
for i in range(n):
    if a[i] < 0:
        minus_counter += 1
        a[i] = -a[i]

if minus_counter % 2 == 0:
    print(sum(a))
else:
    print(sum(a) - 2 * min(a))