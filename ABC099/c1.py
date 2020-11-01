n = int(input())

all_procedure = []
all_procedure.append(1)
for i in range(1, 6):
    all_procedure.append(9 ** i)

for i in range(1, 7):
    all_procedure.append(6 ** i)

all_procedure.sort()

num = len(all_procedure)

counter = 0
while n >= 15:
    l = 0
    r = num - 1
    while l + 1 != r:
        mid = (l + r) // 2
        if n == all_procedure[mid]:
            counter += 1
            n -= all_procedure[mid]
            break
        elif n < all_procedure[mid]:
            r = mid
        elif mid < n:
            l = mid

    n -= all_procedure[l]
    counter += 1
if n % 9 + n // 9 > n % 6 + n // 6:
    print(counter + n // 6 + n % 6)
else:
    print(counter + n // 9 + n % 9)
print(all_procedure)
