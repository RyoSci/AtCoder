s = input()

res = 1000
for i in range(len(s) - 2):
    tmp = int(s[i : i + 3])
    res = min(res, abs(tmp - 753))
print(res)