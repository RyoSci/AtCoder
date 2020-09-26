n = int(input())
s = []
for i in range(n):
    si = input()
    s.append(si)

s_90 = [["" for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        s_90[j][n - 1 - i] = s[i][j]

for i in range(n):
    print("".join(s_90[i]))
