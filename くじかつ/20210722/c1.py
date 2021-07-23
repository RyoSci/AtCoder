n, k = map(int, input().split())


def cal(a):
    r = min(n, a-1)
    l = max(1, a-n)
    return r-l+1


res = 0
for y in range(2, 2*n+1):
    x = k+y
    if 2 <= x <= 2*n:
        res += cal(x)*cal(y)

print(res)
