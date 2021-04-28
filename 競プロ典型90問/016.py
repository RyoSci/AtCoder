n = int(input())
a, b, c = list(map(int, input().split()))

ans = 10 ** 4
for i in range(10 ** 4):
    rest = 10 ** 4 - i
    for j in range(rest):
        tmp = n - a * i - b * j
        if tmp % c == 0 and 0 <= tmp // c < 10 ** 4:
            ans = min(ans, i + j + tmp // c)

print(ans)
