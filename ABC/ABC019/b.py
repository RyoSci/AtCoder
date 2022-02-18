s = input()
res = ""
tmp = s[0]
for i in s[1:]:
    if i != tmp[0]:
        res += tmp[0]
        res += str(len(tmp))
        tmp = i
    else:
        tmp += i
res += tmp[0]
res += str(len(tmp))
print(res)
