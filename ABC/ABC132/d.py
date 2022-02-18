n, k = map(int, input().split())
mod = 10**9+7


def cal(ball, wall):
    # n = ball+wall
    # tmp = 1
    # for i in range(1, n+1):
    #     tmp = tmp * i %mod
    # for i in range(1, ball+1):
    #     tmp = tmp * pow(i, mod-2, mod) %mod
    # for i in range(1, wall+1):
    #     tmp = tmp * pow(i, mod-2, mod) %mod
    # return tmp

    n = ball+wall
    k = min(ball, wall)
    tmp = 1
    for i in range(n, n-k, -1):
        tmp = tmp*i % mod

    for i in range(k, 0, -1):
        tmp = tmp*pow(i, mod-2, mod) % mod

    return tmp


for i in range(1, k+1):
    blue = cal(k-i, i-1)
    if n-k-i+1 < 0:
        print(0)
        continue
    red = cal(n-k-i+1, i)
    print(blue*red % mod)
