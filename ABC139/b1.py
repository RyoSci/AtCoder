a, b = map(int, input().split())
if b == 1:
    print(0)
else:
    b -= a
    counter = 1
    while b > 0:
        b -= a - 1
        counter += 1

    print(counter)

# sum_tap = 1

# for i in range(100):
#     if sum_tap >= b:
#         print(i)
#         break
#     sum_tap += a - 1

