s = input()
k = int(input())

ans = 0
if len(s) < k:
    print(ans)
    exit()

res = set()
for i in range(len(s) - k + 1):
    pathword = ""
    for j in range(i, i + k):
        pathword += s[j]
    res.add(pathword)

print(len(res))
