n = int(input())
c = input()

res = 1000
commands = "ABXY"
for li in commands:
    for lj in commands:
        l = li + lj        
        for ri in commands:
            for rj in commands:
                r = ri + rj
                if l == r:
                    continue
                short_cuts = c.replace(l, "L")
                short_cuts = short_cuts.replace(r, "R")
                res = min(res, len(short_cuts))

print(res)