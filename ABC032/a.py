a = int(input())
b = int(input())
n = int(input())

for i in range(n, 10 ** 7):
    if i % a == i % b == 0:
        print(i)
        exit()
