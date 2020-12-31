x, y = map(int, input().split())

up = (2 * y - x) // 3
right = (2 * x - y) // 3

if x == right * 2 + up and y == right + up * 2 and right >= 0 and up >= 0:
    pass
else:
    print(0)
    exit()
up, right = sorted([up, right])

mod = 10 ** 9 + 7


def div(a, b):
    ans = a
    rest = 1
    while 1:
        if b == 1:
            return rest * ans % mod
        if b % 2 == 1:
            rest = rest * ans % mod
        ans = (ans % mod) ** 2 % mod
        b = b // 2


ans = 1
for i in range(up + right, up + right - up, -1):
    ans = ans * i % mod

for i in range(1, up + 1):
    ans = ans * div(i, mod - 2) % mod

print(ans)
