s = input()
res = 0
si = ""
si_1 = ""
for i in s:
    si_1 += i
    if si != si_1:
        res += 1
        si = si_1
        si_1 = ""
print(res)
