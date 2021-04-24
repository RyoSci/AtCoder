n = int(input())
a = list(map(int, input().split()))

# debag
# n = 20
# a = [2 ** i for i in range(29, 29 - n, -1)]

ans = 2 ** 30
for i in range(1 << n - 1):
    a_xor = 0
    a_or = 0
    for j in range(n - 1):
        a_or |= a[j]
        if i >> j & 1:
            a_xor ^= a_or
            a_or = 0
    a_or |= a[-1]
    a_xor ^= a_or

    ans = min(ans, a_xor)

print(ans)
