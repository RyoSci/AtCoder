n, s = input().split()
n = int(n)

res = 0
for i in range(n - 1):
    agct = dict()
    for k in "AGCT":
        if k not in agct:
            agct[k] = 0
    agct[s[i]] += 1
    for j in range(i + 1, n):
        agct[s[j]] += 1
        a = agct["A"]
        g = agct["G"]
        c = agct["C"]
        t = agct["T"]
        if (a - t == 0) and (c - g == 0) and (a > 0 or c > 0):
            res += 1

print(res)
