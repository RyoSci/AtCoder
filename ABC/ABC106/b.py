n = int(input())
res = 0
for i in range(1, n + 1, 2):
    counter = 0
    for j in range(1, int(i ** (1/2)) + 1):
        if i % j == 0:
            counter += 1
            if i // j != j:
                counter += 1
    if counter == 8:
        res += 1

print(res)
