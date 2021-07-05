p = int(input())
res = 1
for i in range(1, 20):
    res *= i
    if res > p:
        res = res//i
        index = i-1
        break

ans = 0
for i in range(index, 0, -1):
    mod = p % res
    ans += p//res
    p = mod
    res //= i
    if mod == 0:
        break

print(ans)
