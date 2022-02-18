n = int(input())
a = list(map(int, input().split()))
rate = [0] * 9
for i in range(n):
    for j in range(8):
        if 400 * j <= a[i] < 400 * (j + 1):
            rate[j] += 1
            break
    else:
        rate[8] += 1

counter = 0
for i in range(8):
    if rate[i] >= 1:
        counter += 1

print(max(1, counter), counter + rate[8])
