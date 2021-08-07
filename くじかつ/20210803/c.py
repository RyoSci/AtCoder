from itertools import combinations

n = int(input())
d = dict()

for i in "MARCH":
    d[i] = 0

for i in range(n):
    s = input()
    if s[0] in "MARCH":
        d[s[0]] += 1

res = 0
for i in combinations("MARCH", 3):
    tmp = 1
    for j in i:
        tmp *= d[j]
    res += tmp

print(res)
