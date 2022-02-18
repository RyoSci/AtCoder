n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]

res = 0
now = 0
for i in range(n - 1, -1, -1):
    ab[i][0] += res
    if ab[i][0] % ab[i][1] != 0:
        tmp = ab[i][1] - ab[i][0] % ab[i][1]
        res += tmp

print(res)
