n = int(input())
vist = [0] * 10 ** 5
res = 0
for i in range(n):
    a = int(input()) - 1
    if vist[a]:
        res += 1
    vist[a] += 1

print(res)
