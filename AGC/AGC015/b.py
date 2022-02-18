s = input()
n = len(s)
res = 0
for i in range(n):
    if s[i] == "U":
        res += n - 1 - i + 2 * i
    else:
        res += i + 2 * (n - 1 - i)

print(res)
