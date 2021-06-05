s = input()
n = len(s)-1
res = 0
for i in range(1 << (n)):
    tmp = s[0]
    for j in range(n):
        if i >> j & 1:
            tmp += "+"
        tmp += s[j+1]
    tmp = tmp.split("+")
    for j in tmp:
        res += int(j)

print(res)
