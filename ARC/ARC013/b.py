c = int(input())

ans = [0] * 3
for i in range(c):
    nml = sorted(list(map(int, input().split())))
    for j in range(3):
        ans[j] = max(ans[j], nml[j])

res = 1
for i in range(3):
    res *= ans[i]

print(res)
