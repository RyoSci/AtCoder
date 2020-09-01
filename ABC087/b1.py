a = int(input())
b = int(input())
c = int(input())
x = int(input())

c_nums = set(50 * i for i in range(c + 1))
res = 0
for i in range(a + 1):
    for j in range(b + 1):
        tmp = x - 500 * i - 100 * j
        if tmp in c_nums:
            res += 1

print(res)
