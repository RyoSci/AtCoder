n = int(input())
counter = 0

for a in range(1, n):
    counter += (n + a - 1) // a - 1

print(counter)
