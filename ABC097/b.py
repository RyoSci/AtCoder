x = int(input())
res = 1
for i in range(2, 40):
    index = 2
    while i ** index <= x:
        res = max(res, i ** index)
        index += 1

print(res)
