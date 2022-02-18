n, s = input().split()
n = int(n)
atcg = [[0 for i in range(4)] for i in range(n + 1)]
res = 0
if s[0] == "A":
    atcg[1][0] = 1
elif s[0] == "T":
    atcg[1][1] = 1
elif s[0] == "C":
    atcg[1][2] = 1
elif s[0] == "G":
    atcg[1][3] = 1
for i in range(1, n):
    atcg[i + 1][0] += atcg[i][0]
    atcg[i + 1][1] += atcg[i][1]
    atcg[i + 1][2] += atcg[i][2]
    atcg[i + 1][3] += atcg[i][3]
    if s[i] == "A":
        atcg[i + 1][0] = atcg[i][0] + 1
    elif s[i] == "T":
        atcg[i + 1][1] = atcg[i][1] + 1
    elif s[i] == "C":
        atcg[i + 1][2] = atcg[i][2] + 1
    elif s[i] == "G":
        atcg[i + 1][3] = atcg[i][3] + 1


for i in range(n - 1):
    for j in range(i + 2, n + 1, 2):
        a = atcg[j][0]-atcg[i][0]
        t = atcg[j][1]-atcg[i][1]
        c = atcg[j][2]-atcg[i][2]
        g = atcg[j][3]-atcg[i][3]
        if (a - t == 0) and (c - g == 0) and (a > 0 or c > 0):
            res += 1

print(res)
