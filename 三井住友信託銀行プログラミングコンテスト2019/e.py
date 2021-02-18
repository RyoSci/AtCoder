n = int(input())
a = list(map(int, input().split()))
rgb = [0, 0, 0]
mod = 10 ** 9 + 7

ans = 1
for i in range(n):
    cnt = 0
    choice = 0
    for j in range(3):
        if a[i] == rgb[j]:
            cnt += 1
            choice = j
    rgb[choice] += 1
    ans = ans * cnt % mod

print(ans)
