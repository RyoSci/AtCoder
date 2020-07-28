n = int(input())

odd_counter = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        odd_counter += 1
print(odd_counter / n)