n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
for i in range(n - 1):
    if a[i + 1] != a[i]:
        b.append(a[i + 1])

res = 0
i = 1
while i < len(b) - 1:
    if not (b[i - 1] <= b[i] <= b[i + 1] or b[i - 1] >= b[i] >= b[i + 1]):
        res += 1
        i += 2
    else:
        i += 1

print(res + 1)
