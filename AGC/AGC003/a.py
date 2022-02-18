s = input()
nwse = dict()
for i in "NWSE":
    if i not in nwse:
        nwse[i] = 0

for i in s:
    nwse[i] += 1

ans = "Yes"
if nwse["N"] >= 1 and nwse["S"] == 0 or nwse["N"] == 0 and nwse["S"] >= 1:
    ans = "No"
if nwse["W"] >= 1 and nwse["E"] == 0 or nwse["W"] == 0 and nwse["E"] >= 1:
    ans = "No"

print(ans)
