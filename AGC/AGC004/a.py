a, b, c = map(int, input().split())
abcd = [a, b, c, a * b * c % 2]
abcd.sort()
res = 1
for i in range(3):
    res *= abcd[i]

print(res)
