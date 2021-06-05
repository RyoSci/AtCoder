a, b, k = map(int, input().split())


def combination(n, k):
    res = 1
    for i in range(n, n-k, -1):
        res *= i
    for i in range(k, 0, -1):
        res //= i
    return res


def dfs(a, b, s, n, i):
    if a == 0 or b == 0:
        return s + "a"*a + "b"*b
    left = combination(a+b-1, a-1)
    right = combination(a+b-1, b-1)

    if k <= left + i:
        res = dfs(a-1, b, s+"a", left, i)
    else:
        res = dfs(a, b-1, s+"b", right, i+left)
    return res


n = combination(a+b, a)

res = dfs(a, b, "", n, 0)
print(res)
