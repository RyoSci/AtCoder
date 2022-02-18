n = int(input())
a = list(map(int, input().split()))

sum_bunbo = 0
for i in range(n):
    sum_bunbo += 1 / a[i]

print(1 / sum_bunbo)
