s = input()
a = [0] * (len(s) + 1)
for i in range(len(s)):
    if s[i] == "<":
        a[i + 1] = a[i] + 1
    else:
        a[i + 1] = 0

for i in range(len(s) - 1, -1, -1):
    if s[i] == ">":
        a[i] = max(a[i + 1] + 1, a[i])

print(sum(a))
