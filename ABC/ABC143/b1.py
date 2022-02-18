n = int(input())
d = list(map(int, input().split()))
sum_mul = sum(d)

recovery = 0
for i in range(n):
    sum_mul -= d[i]
    recovery += d[i] * sum_mul

print(recovery)
