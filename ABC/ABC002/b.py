w = input()
res = ""
aiueo = "aiueo"
for i in w:
    if i in aiueo:
        continue
    else:
        res += i
print(res)
