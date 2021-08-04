n = int(input())
d = [[0]*26 for _ in range(n)]

for i in range(n):
    s = input()
    for si in s:
        d[i][ord(si)-ord("a")] += 1

res = ""
for i in range(26):
    num = 10**18
    for j in range(n):
        num = min(num, d[j][i])
    res += chr(i+ord("a"))*num

print(res)
