n = int(input())
s = []
for i in range(n):
    si = input()
    s.append(si)

for i in range(n):
    res = ""
    for j in range(n):
        res += s[n - 1 - j][i]
    print(res)
