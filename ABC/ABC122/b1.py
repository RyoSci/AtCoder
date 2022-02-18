s = input()
res = 0
max_res = 0
for i in s:
    if i in "ACGT":
        res += 1
    else:
        res = 0
    max_res = max(max_res, res)

print(max_res)
