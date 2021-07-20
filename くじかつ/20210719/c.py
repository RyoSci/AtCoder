n = int(input())
x = list(map(int, input().split()))

# n = 49
# x = [i for i in range(2, 51)]


def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return 0
    return x


tmp = []
for i in range(2, 51):
    if prime(i):
        tmp.append(i)

m = len(tmp)

ans = 1
for _ in tmp:
    ans *= _

for i in range(1 << m):
    res = []
    for j in range(m):
        if i >> j & 1:
            res.append(tmp[j])
    for j in range(n):
        flag = False
        for k in res:
            if x[j] % k == 0:
                flag = True
        if not flag:
            break
    else:
        cnt = 1
        for _ in res:
            cnt *= _
        ans = min(ans, cnt)
print(ans)
