s  = input()
l = int(s[0]) * 10 + int(s[1])
r = int(s[2]) * 10 + int(s[3])

res = "NA"
if l == 0:
    if 1 <= r <= 12:
        res = "YYMM"
    else:
        res = "NA"
elif 1 <= l <= 12:
    if 1 <= r <= 12:
        res ="AMBIGUOUS"
    else:
        res = "MMYY"
else:
    if 1 <= r <= 12:
        res = "YYMM"
    else:
        res = "NA"

print(res)
