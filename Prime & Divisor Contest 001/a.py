n, a, b = map(int, input().split())


def cal(x):
    tmp = 0
    for i in range(1, x+1):
        if x % i == 0:
            tmp += 1
    return tmp


res = 0
for x in range(1, n+1):
    tmp = cal(x)
    if x % 2 == 1 and tmp == a:
        res += 1
    elif x % 2 == 0 and tmp == b:
        res += 1

print(res)
