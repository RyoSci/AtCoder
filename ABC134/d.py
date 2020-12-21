n = int(input())
a = [-1] + list(map(int, input().split()))
# n = 2 * 10 ** 5
# a = [-1] + [1] * n
b = [0] * (n + 1)

for i in range(n, 0, -1):
    mul = 2
    while i * mul <= n:
        b[i] = (b[i] + b[i * mul]) % 2
        mul += 1
    if b[i] != a[i]:
        b[i] = 1
    else:
        b[i] = 0

ans = []
for i in range(1, n + 1):
    if b[i] == 1:
        ans.append(i)

if ans == []:
    print(0)
else:
    print(len(ans))
    print(*ans)
