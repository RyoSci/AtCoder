l = int(input())


def cal(n, k):
    tmp = 1
    m = n+k
    for i in range(m, n, -1):
        tmp *= i
    for i in range(k, 0, -1):
        tmp //= i
    return tmp


res = cal(l-12, 11)
print(res)
