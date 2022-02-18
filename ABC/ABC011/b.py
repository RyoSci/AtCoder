s = input()
res = ""
for i in range(len(s)):
    if i == 0:
        res += s[i].upper()
    else:
        res += s[i].lower()

print(res)
