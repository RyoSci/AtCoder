n, k = map(int, input().split())
s = input()

res = 0
for i in range(n - 1):
    if s[i + 1] == s[i]:
        res += 1

print(min(res + 2 * k, n - 1))
