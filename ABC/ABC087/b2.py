a = int(input())
b = int(input())
c = int(input())
x = int(input())


def binary_search(x, c_nums):
    l = 0
    r = c
    while l + 1 != r and c != 0:
        m = (l + r) // 2
        if c_nums[m] == x:
            return 1
        elif c_nums[m] < x:
            l = m
        elif c_nums[m] > x:
            r = m
        m = (l + r) // 2
    if x == c_nums[l] or x == c_nums[r]:
        return 1
    else:
        return 0


c_nums = [50 * i for i in range(c + 1)]
res = 0
for i in range(a + 1):
    for j in range(b + 1):
        tmp = x - 500 * i - 100 * j
        res += binary_search(tmp, c_nums)

print(res)
