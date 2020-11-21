n = int(input())
a = list(map(int, input().split()))

total_set_sum = 3 ** n
all_odd_mul = 1
for i in range(n):
    all_odd_mul *= 2 - a[i] % 2

print(total_set_sum - all_odd_mul)
