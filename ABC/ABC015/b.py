n = int(input())
a = list(map(int, input().split()))
not_zero = 0
bags = 0
for i in range(n):
    if a[i] != 0:
        not_zero += 1
        bags += a[i]

print((bags + not_zero - 1) // not_zero)
