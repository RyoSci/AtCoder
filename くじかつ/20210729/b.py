ref = "CODEFESTIVAL2016"
s = input()

res = 0
for i in range(16):
    if s[i] != ref[i]:
        res += 1

print(res)
