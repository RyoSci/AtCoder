n = int(input())
n = 2025 - n
for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                print(str(i) + " x " + str(j))
