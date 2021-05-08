n, m, p = map(int, input().split())


def cal(n, p, rest):
    if p == 1:
        return n * rest % m
    if p % 2 == 1:
        rest = rest * n % m
    return cal(n**2 % m, p//2, rest)


print(cal(n, p, 1))
