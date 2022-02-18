n = int(input())
s = input()
res = 0
for i in range(1, n - 1):
    l = set(s[:i])
    r = set(s[i:])
    tmp = 0
    for j in range(26):
        if chr(ord("a") + j) in l and chr(ord("a") + j) in r:
            tmp += 1
    res = max(res, tmp)
print(res)
