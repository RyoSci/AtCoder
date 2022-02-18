n = int(input())
a = list(map(int, input().split()))
rate = [0] * 9
for i in range(n):
    if a[i] < 400:
        rate[0] += 1
    elif a[i] < 800:
        rate[1] += 1
    elif a[i] < 1200:
        rate[2] += 1
    elif a[i] < 1600:
        rate[3] += 1
    elif a[i] < 2000:
        rate[4] += 1
    elif a[i] < 2400:
        rate[5] += 1
    elif a[i] < 2800:
        rate[6] += 1
    elif a[i] < 3200:
        rate[7] += 1
    else:
        rate[8] += 1

counter = 0
for i in range(8):
    if rate[i] >= 1:
        counter += 1


print(max(1, counter), counter + rate[8])
