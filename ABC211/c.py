s = input()
d = [0]*8
mod = 10**9+7

for i in s:
    if i == "c":
        d[0] += 1
        d[0] %= mod
    elif i in "chokudai":
        for index, j in enumerate("chokudai"):
            if i == j:
                break
        d[index] += d[index-1]
        d[index] %= mod

print(d[-1])
