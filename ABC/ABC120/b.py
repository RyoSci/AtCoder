a, b, k = map(int, input().split())
counter = 0
for i in range(100, 0, -1):
    if a % i == 0 and b % i == 0:
        counter += 1
    if counter == k:
        break

print(i)