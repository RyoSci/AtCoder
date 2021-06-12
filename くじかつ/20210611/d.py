a, b = map(int, input().split())


def g(x, i):
    x += 1
    return x//2**(i+1)*(2**i) + max(0, x % 2**(i+1)-2**i)


res = 0
for i in range(41):
    res += ((g(b, i) - g(a-1, i)) % 2)*2**i

print(res)
