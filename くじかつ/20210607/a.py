s = input()
res = 0
tmp = 0
for i in range(3):
    if s[i] == "R":
        tmp += 1
    else:
        res = max(res, tmp)
        tmp = 0
print(max(res, tmp))
