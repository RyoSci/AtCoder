n = int(input())
for i in range(1, 101):
    if n <= i**2:
        break
print(i**2-n)
