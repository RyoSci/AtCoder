a, b, k = map(int, input().split())


def dfs(a, b, s, n, i):
    if a == 0 or b == 0:
        return s + "a"*a + "b"*b
    left = a*n//(a+b)
    right = b*n//(a+b)

    if k <= left + i:
        res = dfs(a-1, b, s+"a", left, i)
    else:
        res = dfs(a, b-1, s+"b", right, i+left)
    return res


n = 1
for i in range(a+b, a, -1):
    n *= i

for i in range(1, b+1):
    n //= i

res = dfs(a, b, "", n, 0)
print(res)
