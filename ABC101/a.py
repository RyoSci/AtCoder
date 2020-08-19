s = input()
res = 0
for i in range(len(s)):
    if s[i] == "+":
        res += 1
    else:
        res -= 1

print(res)