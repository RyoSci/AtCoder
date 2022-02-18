n = int(input())
dictionay = dict()
for i in range(n):
    s = input()
    dictionay[s] = 1

for tmp in dictionay.keys():
    if tmp in dictionay and "!"+tmp in dictionay:
        ans = tmp
        break
else:
    ans = "satisfiable"

print(ans)
