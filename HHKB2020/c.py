n = int(input())
p = list(map(int, input().split()))
num = [1] * (2 * 10 ** 5 + 1)

now = 0
for i in range(n):
    num[p[i]] = 0
    if num[now] == 1:
        print(now)
    else:
        while num[now] != 1:
            now += 1
        print(now)
