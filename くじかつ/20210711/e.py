n, m = map(int, input().split())

array = [10**18]*(1 << n)


def cal(c):
    tmp = 0
    c = c[::-1]
    for i in range(len(c)):
        if c[i] == 1:
            tmp += 2**(i)
    return tmp


for i in range(m):
    a, b = map(int, input().split())
    _ = list(map(int, input().split()))
    c = [0]*n
    for j in range(b):
        c[_[j]-1] = 1
    index = cal(c)
    array[index] = min(array[index], a)

res = [10**18]*n
ans = sum(res)

for i in range(1 << n):
    tmp = res[:]
    flag = True
    for j in range(n):
        if i >> j & 1:
            if flag:
                tmp[j] = array[i]
                flag = False
            else:
                tmp[j] = 0
    if sum(res) > sum(tmp):
        res = tmp[:]

if 10**18 in res:
    print(-1)
else:
    print(sum(res))

print(res)
# print(array)
