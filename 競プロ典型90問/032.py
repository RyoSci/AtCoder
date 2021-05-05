from itertools import permutations
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
ng = set()
for i in range(m):
    x, y = map(int, input().split())
    ng.add(str(x-1)+str(y-1))
    ng.add(str(y-1)+str(x-1))

res = 1000*10 + 1
for i in permutations(range(n)):
    for j in range(n-1):
        if str(i[j]) + str(i[j+1]) in ng:
            break
    else:
        tmp = 0
        for j in range(n):
            tmp += a[i[j]][j]
        res = min(res, tmp)

if res == 10001:
    res = -1

print(res)
