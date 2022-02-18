s = input()
d = {"6": "9", "9": "6"}

res = ""
for i in s:
    if i in d:
        res += d[i]
    else:
        res += i
print(res[::-1])
