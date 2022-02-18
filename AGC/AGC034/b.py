s = input()
n = len(s)
ans = 0
a = 0
i = 0
while i < n - 1:
    if s[i] == "A":
        a += 1
    elif s[i] == "B" and s[i + 1] == "C":
        ans += a
        i += 1
    else:
        a = 0
    i += 1

print(ans)
