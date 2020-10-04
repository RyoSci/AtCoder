n, k = map(int, input().split())
d = list(map(int, input().split()))
avairable_num = []
for i in range(0, 10):
    if i not in d:
        avairable_num.append(i)
n = str(n)

res = ""
additional = False
for i in range(len(n)):
    for j in avairable_num:
        if int(n[i]) == j:
            res += str(j)
            break
        elif int(n[i]) < j:
            res += str(j)
            additional = True
            break
    else:
        if i == 0:
            for j in avairable_num:
                if j != 0:
                    res += str(j)
                    break
            res += str(avairable_num[0])
            additional = True
    if additional:
        break
if additional:
    while len(res) < len(n):
        res += str(avairable_num[0])
if int(res) < int(n):
    res += str(avairable_num[0])
print(res)
