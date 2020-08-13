k = int(input())

res = 0
for i in range(1, k + 1):
    for j in range(1, k + 1):
        if i % 2 == 0 and j % 2 == 1:
            res += 1
print(res)